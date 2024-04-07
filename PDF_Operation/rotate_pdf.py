"""
rotate_pdf.py

Rotates a selected PDF file by a specific angle.

Description:
This module provides a command-line interface to rotate a selected PDF file by a specific angle.
It uses the argparse module for command-line argument parsing, tkinter for GUI file dialog,
and the pdf_operation module for PDF file operations.
The rotation angle and file to process can be provided as command-line arguments or retrieved from the config module.
"""

from tkinter import filedialog

from config import rotation_angle, file_show_file_dialog, file_input_file
from pdf_operation import PdfOperation


def main():
    if file_show_file_dialog == 1:
        file = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
    else:
        file = file_input_file
    print(f'Folder: {file}')
    pdf_ops.rotate_pdf(file, rotation_angle)
    print('Rotation angle:', rotation_angle)


if __name__ == '__main__':
    pdf_ops = PdfOperation()
    main()
