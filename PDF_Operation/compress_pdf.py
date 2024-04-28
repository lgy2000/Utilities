# !/usr/bin/env python3

"""
compress_pdf.py

Compresses a specific PDF file using pycpdflib.

Description:
This module provides a command-line interface to compress a selected PDF file. It uses the argparse module for command-line argument parsing,
tkinter for GUI file dialog, and the pdf_operation module for PDF file operations. The file to process can be provided as a command-line argument
or retrieved from the config module.
"""

import argparse
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from PDF_Operation.pdf_operation import PdfOperation
from config import file_input_file
from config import file_show_file_dialog

logging_load_human_config()


def main():
    try:
        pdf_ops = PdfOperation()
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", type=str, help="File to process")
        args = parser.parse_args()

        if not args.file:
            if file_show_file_dialog == 1:
                file = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
                if not file:
                    raise SystemExit("No input file selected.")
            else:
                file = file_input_file
        else:
            file = args.file
        print(f'File: {file}')

        pdf_ops.compress_pdf(file)
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
