"""
get_title_from_pdf.py

Extracts the title from a PDF file.

Description:
This module uses the PdfOperation class from the pdf_operation module to extract the title from a PDF file. The title is determined by a keyword
that is passed to the get_title_from_pdf method. The module can either prompt the user to select a file or use a predefined file path.
"""

# !/usr/bin/env python3
import argparse
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from PDF_Operation.pdf_operation import PdfOperation
from config import file_show_file_dialog, pdf_input_file

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
                file = pdf_input_file
        else:
            file = args.file
        keyword = "Title"
        title = pdf_ops.get_title_from_pdf(file, keyword)
        if title:
            print("Title:", title)
        else:
            print("Title not found.")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
