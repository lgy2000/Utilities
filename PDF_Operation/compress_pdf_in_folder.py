# !/usr/bin/env python3

"""
compress_pdf_in_folder.py

Compresses all PDF files in a given folder, and save the compressed files in a new folder.

Description:
This module provides functionality to compress all PDF files in a given folder. It uses the pdf_operation module for PDF file operations and the
config module for configuration settings.
"""

import argparse
import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

from File_Operation.file_operation import FileOperation
from pdf_operation import PdfOperation

logging_load_human_config()


def main():
    try:
        pdf_ops = PdfOperation()
        file_ops = FileOperation()
        parser = argparse.ArgumentParser()
        parser.add_argument("--folder", type=str, help="Folder to process")
        args = parser.parse_args()

        if not args.folder:
            _, folder = file_ops.copy_folder_and_files()  # If no folder is provided, open a file dialog to select a folder
        else:
            folder = args.folder

        pdf_ops.loadDLL_libpycpdf()
        pdf_ops.compress_pdf_in_folder(folder)
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
