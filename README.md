# PDF Shortener Script

This Python-Script shortens a PDF-file that has page-numbers written in it by only keeping unique pages.

## Requirements

Install required libraries:
   ```bash
   pip install fitz
   pip install PyMuPDF
   ```

## Usage

1. Put the PDF-file you want to shorten in the `PDFs` folder.
2. Start the script.
3. Enter the name of your PDF-file in the format `<name>.pdf` when prompted to.

The script creates a new, shortened version of your PDF and saves it in the same folder. It has the same name as the original with the added prefix `"no_duplicates_"`.

## Notice
- On Arch Linux you only need to install `PyMuPDF` with this command:
  ```bash
  sudo pacman -S python-PyMuPDF
