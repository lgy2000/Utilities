#!/usr/bin/env python3

"""
compress_pdf_ilovepdf.py

This module is used for compressing a selected PDF file using the iLovePDF API.

Description:
This module reads the public keys from a configuration file, asks the user to select a PDF file, and then compresses the selected file using the
iLovePDF API. The compressed file is saved with a specific naming pattern.
"""

import configparser
import logging
import os
from tkinter import filedialog

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
compressed_pdfs_pattern = "*compress*.pdf"
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
    action_path = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])

    # Compress all PDF files in the subdirectory
    pdf_ops.compress_pdf_file_ilovepdf(action_path, compress_level, compressed_pdfs_pattern, output_errors, public_key1, public_key2, public_key3)


if __name__ == '__main__':
    main()
