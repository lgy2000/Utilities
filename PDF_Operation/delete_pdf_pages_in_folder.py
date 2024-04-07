"""
delete_pdf_pages_in_folder.py

Deletes specific pages from all PDF files in a given folder.

Description:
This module provides functionality to delete specific pages from all PDF files in a given folder.
It uses the pdf_operation module for PDF file operations and the config module for configuration settings.
"""

import argparse

from File_Operation.copy_folder import copy_folder
from config import pdf_input_folder, page_number
from pdf_operation import PdfOperation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page_number", type=int, help="Page number to delete")
    parser.add_argument("--folder", type=str, help="Folder to process")
    args = parser.parse_args()

    # Use the page_number from args if it's not None, otherwise use the one from config
    delete_page_number = args.page_number if args.page_number is not None else page_number
    if not args.folder:
        _, folder = copy_folder(pdf_input_folder)
    else:
        folder = args.folder

    pdf_ops.delete_pdf_page_in_folder(folder, delete_page_number)
    print(f'Delete number of pages: {delete_page_number}')


if __name__ == '__main__':
    pdf_ops = PdfOperation()
    main()
