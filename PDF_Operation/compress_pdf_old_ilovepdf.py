#!/usr/bin/env python3

"""
compress_pdf_old_ilovepdf.py

This module is used for compressing old PDF files in a selected folder using the iLovePDF API.

Description:
This module reads the public keys from a configuration file, asks the user to select a folder, finds old PDF files in the selected folder,
and then compresses these files using the iLovePDF API. The compressed files are saved with a specific naming pattern.
"""

import configparser
import logging
import os
from tkinter import filedialog

from find_old_pdf import main as find_old_pdf
from pdf_operation import PdfOperation

# Create a logger
logger = logging.getLogger()

# Create a handler for the DEBUG level messages
debug_handler = logging.FileHandler(r"D:\YK\Resources\PDF Compression Debugging.log")
debug_handler.setLevel(logging.DEBUG)
logger.addHandler(debug_handler)

# Create a handler for the INFO level messages
info_handler = logging.FileHandler(r"D:\YK\Resources\PDF Compression.log")
info_handler.setLevel(logging.INFO)
logger.addHandler(info_handler)

# Set the logger level to the lowest level handler
logger.setLevel(logging.INFO)

# Define constants
compress_level = 'compress'  # low, compress, extreme
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
all_pdfs_pattern = "*.pdf"
compressed_pdfs_pattern = "*compress*.pdf"
compressed_zip_pattern = "*compress*.zip"
compressed_file_regex_pattern = r"_compress_\d\d\-\d\d\-\d\d\d\d"
compressed_file_regex_pattern2 = r"_compress"
output_errors = ""

# Read the configuration file to get the public key
config = configparser.ConfigParser()
config.read(r"..\config.ini")
public_key1 = config['ILOVEPDF_USER_INFO']['PUBLIC_KEY1']
public_key2 = config['ILOVEPDF_USER_INFO']['PUBLIC_KEY2']
public_key3 = config['ILOVEPDF_USER_INFO']['PUBLIC_KEY3']


def main():
    pdf_ops = PdfOperation()
    # Ask the user to select a directory
    action_path = filedialog.askdirectory()

    old_file_path = find_old_pdf(action_path)
    compressed_done = 0

    if old_file_path:
        print(f"Old PDF files found: {len(old_file_path)}")
        for file_path in old_file_path:
            # Compress all PDF files in the subdirectory
            pdf_ops.compress_pdf_file_ilovepdf(file_path, compress_level, compressed_pdfs_pattern, output_errors, public_key1, public_key2,
                                               public_key3)
            compressed_done += 1

    print(f"Old PDF files found compressed: {compressed_done}")


if __name__ == '__main__':
    main()
