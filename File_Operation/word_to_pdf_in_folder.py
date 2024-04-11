"""
word_to_pdf_in_folder.py

Module for converting Word documents in a specified folder to PDF format.

Description:
This module provides functionality to convert all Word documents within a selected folder into PDF files. It uses the `tkinter` library for GUI
functionality to prompt the user to select a folder and the `docx2pdf` library for the conversion process. The `word_to_pdf_in_folder()` function
is the main function that initiates the conversion process. If the `show_folder_dialog` configuration is enabled, it prompts the user to select a
folder via a GUI dialog, otherwise, it uses the `input_folder` specified in the configuration. The function then converts all Word files in the
selected folder into PDF files and saves them in the same folder. The `main()` function is provided for standalone execution, which initiates the
Word to PDF conversion process and prints "done" upon completion.
"""

# !/usr/bin/env python3
import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

from config import file_input_folder
from file_operation import FileOperation

logging_load_human_config()


def main():
    try:
        file_ops = FileOperation()
        file_ops.word_to_pdf_in_folder(file_input_folder)
        print('Folder: ', file_input_folder)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
