# PPT to PDF Converter with Video Support

A Python-based tool that converts PowerPoint presentations to PDF while handling embedded videos and providing a user-friendly GUI interface.

## Features

- 🖥️ User-friendly GUI interface for easy file selection
- 📄 Converts PPTX files to PDF format
- 🎥 Handles presentations with embedded videos
- 🔄 Automatic video URL extraction
- 💫 Video shape overlay support
- 🖥️ Cross-platform support (macOS, with Windows and Linux support coming soon)

## Prerequisites

- Python 3.7 or higher
- LibreOffice (currently bundled only for macOS)
- Required Python packages (install via pip):
  ```bash
  python-pptx
  tkinter
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pptToPdf.git
   cd pptToPdf
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   .\venv\Scripts\activate  # On Windows
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the GUI converter:
   ```bash
   python gui_converter.py
   ```

2. In the GUI:
   - Click "Select Input Directory" to choose the folder containing your PPTX files
   - Click "Select Output Directory" to choose where to save the converted PDFs
   - Click "Convert" to start the conversion process

## Project Structure

- `gui_converter.py`: Main GUI application
- `libreoffice.py`: LibreOffice integration and PDF conversion
- `extract_video_url.py`: Video URL extraction from PPTX files
- `overlay_video_with_shape.py`: Video shape manipulation
- `libreoffice/`: Directory containing LibreOffice binaries

## Todo Tasks

Feel free to contribute to any of these tasks by submitting a pull request:

### High Priority
- [ ] Add LibreOffice binaries for Windows
- [ ] Add LibreOffice binaries for Linux
- [ ] Add progress bar in GUI during conversion
- [ ] Implement batch processing for multiple directories

### Medium Priority
- [ ] Add support for custom PDF output naming
- [ ] Implement conversion settings (quality, compression)
- [ ] Add logging system for better debugging
- [ ] Create automated tests

### Low Priority
- [ ] Add dark mode to GUI
- [ ] Create standalone executable packages
- [ ] Add support for older PowerPoint formats
- [ ] Implement conversion preview

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines for Contributing LibreOffice Binaries
- Windows binaries should be added to `libreoffice/windows/`
- Linux binaries should be added to `libreoffice/linux/`
- Ensure binaries are compatible with the latest LibreOffice version
- Include installation verification scripts
- Document any specific OS version requirements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LibreOffice for providing the core conversion functionality
- Python-PPTX library for PowerPoint file manipulation
- All contributors who help improve this project

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues in the GitHub repository
2. Create a new issue if your problem hasn't been reported
3. Provide detailed information about your system and the error message
