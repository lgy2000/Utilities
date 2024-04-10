"""
rotate_pdf_in_folder.py

Rotates all PDF files in a given folder by a specific angle.

Description:
This module provides functionality to rotate all PDF files in a given folder by a specific angle.
It uses the pdf_operation module for PDF file operations and the config module for configuration settings.
"""

from File_Operation.file_operation import FileOperation
from config import pdf_input_folder, rotation_angle
from pdf_operation import PdfOperation

import argparse
from tkinter import filedialog

from config import rotation_angle, file_show_file_dialog, file_input_file
from pdf_operation import PdfOperation



def main():
    pdf_ops = PdfOperation()
    file_ops = FileOperation()
    parser = argparse.ArgumentParser()
    parser.add_argument("--rotation_angle", type=int, help="Rotation angle in degrees")
    parser.add_argument("--file", type=str, help="File to process")
    args = parser.parse_args()

    # Use the rotation_angle from args if it's not None, otherwise use the one from config
    _rotation_angle = args.rotation_angle if args.rotation_angle is not None else rotation_angle
    if not args.file:
        _, folder = file_ops.copy_folder(pdf_input_folder)
    else:
        folder = args.folder
    pdf_ops.rotate_pdf_in_folder(folder, rotation_angle)
    print('Rotation angle:', rotation_angle)


if __name__ == '__main__':
    main()
