import os
import subprocess
import platform


# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
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


def convert_to_pdf(input_file):
    """Convert a single PPTX file to PDF using LibreOffice."""
    libreoffice_path = get_libreoffice_path()
    cmd = [
        libreoffice_path,
        "--headless",  # Run in headless mode (no GUI)
        "--convert-to", "pdf",  # Convert to PDF format
        "--outdir", OUTPUT_DIR,  # Save PDF in the output directory
        input_file,  # Input file
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {input_file} -> {OUTPUT_DIR}")

        # Check if the PDF file has been created
        pdf_file = input_file.replace(".pptx", ".pdf")
        if os.path.exists(pdf_file):
            print(f"PDF created: {pdf_file}")
            # Delete the .pptx file after conversion
            os.remove(input_file)
            print(f"Deleted original PPTX file: {input_file}")
        else:
            print(f"PDF not created for: {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_file}: {e.stderr.decode('utf-8')}")


def ensure_directories():
    """Ensure the output directory exists."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


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
            convert_to_pdf(input_path)

    print(f"All conversions completed. PDFs saved in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()