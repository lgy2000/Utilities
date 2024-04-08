"""
rotate_pdf_in_folder.py

Rotates all PDF files in a given folder by a specific angle.

Description:
This module provides functionality to rotate all PDF files in a given folder by a specific angle.
It uses the pdf_operation module for PDF file operations and the config module for configuration settings.
"""

from File_Operation.copy_folder import copy_folder
from config import pdf_input_folder, rotation_angle
from pdf_operation import PdfOperation


def main():
    pdf_ops = PdfOperation()
    _, folder2 = copy_folder(pdf_input_folder)
    pdf_ops.rotate_pdf_in_folder(folder2, rotation_angle)
    print('Rotation angle:', rotation_angle)


if __name__ == '__main__':
    main()
