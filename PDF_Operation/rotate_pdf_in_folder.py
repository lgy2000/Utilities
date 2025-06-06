# !/usr/bin/env python3

"""
rotate_pdf_in_folder.py

Rotates all PDF files in a given folder by a specific angle.

Description:
This module provides functionality to rotate all PDF files in a given folder by a specific angle.
It uses the pdf_operation module for PDF file operations and the config module for configuration settings.
"""

import argparse
import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

from File_Operation.file_operation import FileOperation
from config import rotation_angle
from pdf_operation import PdfOperation

logging_load_human_config()


def main():
    try:
        pdf_ops = PdfOperation()
        file_ops = FileOperation()
        parser = argparse.ArgumentParser()
        parser.add_argument("--folder", type=str, help="Folder to process")
        parser.add_argument("--rotation_angle", type=int, help="Rotation angle in degrees")
        args = parser.parse_args()

        # Use the rotation_angle from args if it's not None, otherwise use the one from config
        rotate_angle = args.rotation_angle if args.rotation_angle is not None else rotation_angle
        if not args.folder:
            _, folder = file_ops.copy_folder_and_files()  # If no folder is provided, open a file dialog to select a folder
        else:
            folder = args.folder

        pdf_ops.rotate_pdf_in_folder(folder, rotate_angle)
        print(f'Rotation angle: {rotate_angle}')
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
