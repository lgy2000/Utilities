# !/usr/bin/env python3

"""
delete_pdf_page.py

Removes specific pages from a PDF file.

Description:
This module provides a command-line interface to remove a specific page from a selected PDF file.
It uses the argparse module for command-line argument parsing, tkinter for GUI file dialog,
and the pdf_operation module for PDF file operations.
The page number and file to process can be provided as command-line arguments or retrieved from the config module.
"""


import argparse
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from PDF_Operation.pdf_operation import PdfOperation
from config import file_show_file_dialog
from config import pdf_page_number, file_input_file

logging_load_human_config()


def main():
    try:
        pdf_ops = PdfOperation()
        parser = argparse.ArgumentParser()
        parser.add_argument("--page_number", type=int, help="Page number to delete")
        parser.add_argument("--file", type=str, help="File to process")
        args = parser.parse_args()

        # Use the page_number from args if it's not None, otherwise use the one from config
        delete_page_number = args.page_number if args.page_number is not None else pdf_page_number
        if not args.file:
            if file_show_file_dialog == 1:
                filename = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
                if not filename:
                    raise SystemExit("No input file selected.")
            else:
                filename = file_input_file
        else:
            filename = args.file

        print(f'File: {filename}')
        pdf_ops.delete_pdf_page(filename, delete_page_number)
        print(f'Delete page: {delete_page_number}')
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
