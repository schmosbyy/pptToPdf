import os
import subprocess
import platform
import shutil


# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
PDF_DIR = os.path.join(BASE_DIR, "pdf")
LIBREOFFICE_DIR = os.path.join(BASE_DIR, "libreoffice")


def get_libreoffice_path():
    """Get the path to the LibreOffice executable based on the OS."""
    system = platform.system().lower()
    if system == "windows":
        return os.path.join(LIBREOFFICE_DIR, "windows", "soffice.exe")
    elif system == "linux":
        return os.path.join(LIBREOFFICE_DIR, "linux", "soffice.AppImage")
    elif system == "darwin":  # macOS
        return os.path.join(LIBREOFFICE_DIR, "macos", "LibreOffice.app", "Contents", "MacOS", "soffice")
    else:
        raise RuntimeError(f"Unsupported operating system: {system}")


def convert_to_pdf(input_file, output_dir):
    """Convert a single PPTX file to PDF using LibreOffice."""
    libreoffice_path = get_libreoffice_path()
    cmd = [
        libreoffice_path,
        "--headless",  # Run in headless mode (no GUI)
        "--convert-to", "pdf",  # Convert to PDF format
        "--outdir", output_dir,  # Output directory
        input_file,  # Input file
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {input_file} -> {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_file}: {e.stderr.decode('utf-8')}")


def ensure_directories():
    """Ensure the output and PDF directories exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)


def main():
    """Main function to process all PPTX files."""
    ensure_directories()
    libreoffice_path = get_libreoffice_path()

    if not os.path.exists(libreoffice_path):
        print(f"LibreOffice not found at {libreoffice_path}. Please ensure the correct binaries are in the 'libreoffice' folder.")
        return

    # Process all .pptx files in the output directory
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".pptx"):
            input_path = os.path.join(OUTPUT_DIR, filename)
            convert_to_pdf(input_path, PDF_DIR)

    print(f"All conversions completed. PDFs saved to {PDF_DIR}")


if __name__ == "__main__":
    main()