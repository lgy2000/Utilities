"""
Module name: delete_pdf_pages_in_folder.py

Description:
Removes specific pages from all PDF files in a folder.

Notes:

The module utilizes the tkinter and pikepdf modules for GUI functionality and PDF manipulation respectively.
The delete_pdf_pages() function prompts the user to select a PDF file via a GUI dialog.
It then removes the page specified by page_number from the selected PDF file.
The modified PDF is saved with a filename appended with " Modified" to distinguish it from the original.
The main() function is provided for standalone execution, which initiates the deletion process and prints "done" upon completion.
"""

import os

import pikepdf

from config import page_number
from copy_folder import copy_folder


def delete_pdf_pages_in_folder(page_number, folder):
    """remove specific pages from all PDF files within a folder"""
    for count, filename in enumerate(os.listdir(folder)):
        filename1 = f'{folder}/{filename}'
        file = pikepdf.Pdf.open(filename1)
        del file.pages[page_number]
        filename2 = f'{folder}/{filename}'
        print(filename2)
        file.save(filename2)


def main():
    _, folder2 = copy_folder()
    delete_pdf_pages_in_folder(page_number, folder2)
    print('done')


if __name__ == '__main__':
    main()
