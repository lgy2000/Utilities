"""
rotate_pdf.py

Rotates a selected PDF file by a specific angle.

Description:
This module provides a command-line interface to rotate a selected PDF file by a specific angle.
It uses the argparse module for command-line argument parsing, tkinter for GUI file dialog,
and the pdf_operation module for PDF file operations.
The rotation angle and file to process can be provided as command-line arguments or retrieved from the config module.
"""

import argparse
from tkinter import filedialog

from config import rotation_angle, file_show_file_dialog, file_input_file
from pdf_operation import PdfOperation


def main():
    pdf_ops = PdfOperation()
    parser = argparse.ArgumentParser()
    parser.add_argument("--rotation_angle", type=int, help="Rotation angle in degrees")
    parser.add_argument("--file", type=str, help="File to process")
    args = parser.parse_args()

    # Use the rotation_angle from args if it's not None, otherwise use the one from config
    _rotation_angle = args.rotation_angle if args.rotation_angle is not None else rotation_angle
    if not args.file:
        if file_show_file_dialog == 1:
            file = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
        else:
            file = file_input_file
    else:
        file = args.file
    print(f'Folder: {file}')
    pdf_ops.rotate_pdf(file, _rotation_angle)
    print('Rotation angle:', _rotation_angle)


if __name__ == '__main__':
    main()
