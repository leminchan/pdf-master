# PDFmaster
PDFmaster is a Python script to merge PDF files together.

## Description
This was done as a personal project to avoid using third-party PDF editors such as PDFmerge. I made the script usage similar to command line arguments to allow for multiple actions with one script.

## Installation
Install the required dependencies, PyPDF2 and argparse.
```bash
pip install PyPDF2
pip install argparse
```

## Usage
usage: 
```bash
py masterpdf.py [-h] [-f [F [F ...]]] [-d D]
```

If you want to merge multiple files in consecutive order, use the -f command as so:
```bash
py masterpdf.py -f pdf_one.pdf pdf_two.pdf ...
```

If you would like to merge all pdf's in a directory, use the -d command as so:
```bash
py masterpdf.py -d directory_containing_pdf
```

Users can chain / use multiple commands in one call!

## Project Status
In the process of adding functions like splitting a PDF, exporting text and images from a PDF, and merging with specified page numbers for PDFmaster.
