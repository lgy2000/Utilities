#!/usr/bin/env python3

"""
compress_pdf_in_folder_ilovepdf_by_parts.py

This module is used for compressing all PDF files in a selected folder in parts using the iLovePDF API.

Description:
This module reads the public keys from a configuration file, asks the user to select a folder, and then compresses all PDF files in the selected
folder in parts using the iLovePDF API. The compressed files are saved with a specific naming pattern.
"""

import configparser
import logging
import os
import shutil
from tkinter import filedialog

from File_Operation.move_folder_to_subfolder_size import move_folder_to_subfolder
from File_Operation.move_subfolder_to_folder import move_subfolder_to_folder
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
    folder = filedialog.askdirectory()
    print(f"Selected directory: {folder}")
    parent_folder_name = os.path.basename(folder)
    all_path = []

    # Define the subfolder name prefix
    subfolder_name = 'subfolder_'
    ignore_folder_prefix = "___"

    try:
        # Move files from the selected directory to subfolders, with a maximum of 25 files per subfolder
        move_folder_to_subfolder(folder, 50, subfolder_name)

        # Walk through the directory tree of the selected directory
        for root, dirs, files in os.walk(folder):
            if dirs:
                # For each subdirectory in the current directory
                for d in dirs:
                    # Exclude subfolder with the specified prefix
                    if not d.startswith(ignore_folder_prefix) and d != parent_folder_name:
                        # Compress all PDF files in the subdirectory
                        subfolder = os.path.join(root, d)
                        pdf_ops.compress_pdf_folder_ilovepdf(subfolder, compress_level, all_pdfs_pattern, compressed_pdfs_pattern,
                                                             compressed_zip_pattern,
                                                             compressed_file_regex_pattern, compressed_file_regex_pattern2, output_errors,
                                                             public_key1, public_key2, public_key3)
                        all_path.append(subfolder)
            if files:
                # For each file in the current directory
                for f in files:
                    # Exclude files with the specified prefix
                    if not f.startswith(ignore_folder_prefix):
                        file = os.path.join(root, f)
                        # Compress all PDF files in the subdirectory
                        pdf_ops.compress_pdf_file_ilovepdf(file, compress_level, compressed_pdfs_pattern, output_errors, public_key1, public_key2,
                                                           public_key3)

                        all_path.append(file)
        print(path for path in all_path)
    except Exception as e:
        print(path for path in all_path)
        print(f"Error: {e}")

    # Move files from subfolders back to the parent directory, but only from subfolders with the specified name prefix
    move_subfolder_to_folder(folder, subfolder_name)

    # Remove unnecessary subfolders
    unnecessary_folders = os.path.join(folder, parent_folder_name)
    if os.path.exists(unnecessary_folders):
        shutil.rmtree(unnecessary_folders)


if __name__ == '__main__':
    main()
