"""
Module name: rotate_pdf_in_folder.py

Description:
Rotates all pages of a PDF file by a specified angle in a folder.

Notes:
- The module relies on the `tkinter` library for GUI functionality to prompt the user to select a PDF file.
- It also utilizes the `PyPDF2` library for PDF manipulation.
- The `rotate_pdf_page()` function rotates each page of the PDF by the specified angle and adds it to the output PDF.
- The `rotate_pdf_pages()` function prompts the user to select a PDF file via a GUI dialog if `show_file_dialog` is enabled, otherwise it uses the
`input_file` specified in the configuration.
- It then opens the input PDF file, rotates each page using the `rotate_pdf_page()` function, and writes the rotated pages to the same file,
effectively overwriting the original PDF.
- The `main()` function orchestrates the PDF rotation process and prints "done" upon completion.
"""

import os

from PyPDF2 import PdfReader, PdfWriter

from config import rotation_angle
from copy_folder import copy_folder
from rotate_pdf import rotate_pdf_page


def rotate_pdf_pages_in_folder(folder, angle):
    # Iterate over each PDF file in the input directory
    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            file = os.path.join(folder, filename)

            # Open the input PDF file
            with open(file, 'rb') as f:
                reader = PdfReader(f)
                writer = PdfWriter()

                rotate_pdf_page(angle, reader, writer)

                # Write the rotated pages to the output PDF file
                with open(file, 'wb') as output_pdf:
                    writer.write(output_pdf)


def main():
    _, folder2 = copy_folder()
    rotate_pdf_pages_in_folder(folder2, rotation_angle)
    print('done')


if __name__ == '__main__':
    main()
