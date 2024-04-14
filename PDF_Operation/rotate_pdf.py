# !/usr/bin/env python3

"""
rotate_pdf.py

Rotates a selected PDF file by a specific angle.

Description:
This module provides a command-line interface to rotate a selected PDF file by a specific angle.
It uses the argparse module for command-line argument parsing, tkinter for GUI file dialog,
and the pdf_operation module for PDF file operations.
The rotation angle and file to process can be provided as command-line arguments or retrieved from the config module.
"""

import argparse
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from config import rotation_angle, file_show_file_dialog, file_input_file
from pdf_operation import PdfOperation

logging_load_human_config()


def main():
    try:
        pdf_ops = PdfOperation()
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", type=str, help="File to process")
        parser.add_argument("--rotation_angle", type=int, help="Rotation angle in degrees")
        args = parser.parse_args()

        # Use the rotation_angle from args if it's not None, otherwise use the one from config
        rotate_angle = args.rotation_angle if args.rotation_angle is not None else rotation_angle
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

        pdf_ops.rotate_pdf(file, rotate_angle)
        print('Rotation angle:', rotate_angle)
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
