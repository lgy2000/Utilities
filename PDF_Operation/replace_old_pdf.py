# !/usr/bin/env python3

"""
replace_old_pdf.py

This module is used for replacing original PDF files with their compressed versions.

Description:
This module asks the user to select a folder, finds all PDF files and their compressed versions in the selected folder, and then replaces the
original files with the compressed ones. If any errors occur during the replacement, they are printed to the console.
"""

import glob
import os
import re
import shutil
import time
from fnmatch import fnmatch
from pathlib import Path
from tkinter import filedialog


# TODO: Move this to the file operation module

def main():
    # Initialize an empty list to store the paths of all PDF files
    pdf_files = []

    # Define the patterns for matching PDF files and compressed PDF files
    all_pdfs_pattern = "*.pdf"
    compressed_pdfs_pattern = "*compress*.pdf"

    # Define the regular expression patterns for matching compressed PDF files
    compressed_file_regex_pattern = r"_compress_\d\d\-\d\d\-\d\d\d\d"
    compressed_file_regex_pattern2 = r"_compressed"

    # Initialize an empty string to store error messages
    output_errors = ""

    # Open a dialog for the user to select a directory
    folder = filedialog.askdirectory()

    # Get the parent path and the name of the selected directory
    action_folder_name = os.path.basename(folder)

    # Walk through the directory tree of the selected directory
    for path, dirs, files in os.walk(folder):
        for file in files:
            # If the file is a PDF file, add its path to the list
            if fnmatch(file, all_pdfs_pattern):
                pdf_files.append(os.path.join(path, file))

    # Check if the path where the zip files are extracted is correct
    wrong_zip_path = str(os.path.join(folder, action_folder_name, action_folder_name))
    correct_zip_path = str(os.path.join(folder, action_folder_name))

    # If the path is not correct, move the files to the correct path
    if os.path.exists(wrong_zip_path):
        for src_dir, dirs, files in os.walk(wrong_zip_path):
            dst_dir = src_dir.replace(wrong_zip_path, correct_zip_path, 1)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    print(f"File already exists: {dst_file}")
                shutil.move(src_file, dst_dir)

    # Wait for the extraction to finish
    time.sleep(3)

    # Find all compressed PDF files in the selected directory
    compressed_pdfs = glob.glob(os.path.join(folder, '**', compressed_pdfs_pattern), recursive=True)

    # Replace the original PDF files with the compressed ones
    for compressed_file_path in compressed_pdfs:
        compressed_file_name = os.path.split(compressed_file_path)[1]

        # Remove the compressed file regex pattern from the compressed file name
        if re.search(compressed_file_regex_pattern, compressed_file_name):
            compressed_file_name = re.sub(compressed_file_regex_pattern, '', compressed_file_name)
        else:
            compressed_file_name = compressed_file_name.replace(compressed_file_regex_pattern2, '')

        file_name = os.path.splitext(compressed_file_name)[0]
        for original_file_path in pdf_files:
            original_file_name = os.path.split(original_file_path)[1]
            original_file_name = os.path.splitext(original_file_name)[0]

            # Determine original file which does not contain "compress" string
            if "compress" not in original_file_name:

                # Remove the folder name from the compressed file name if exists
                folder_name = os.path.split(os.path.split(original_file_path)[0])[1]
                if folder_name in compressed_file_name:
                    # the folder name (potentially followed by one or two characters ??), is replaced with an empty string
                    compressed_file_name = re.sub(f"{folder_name}??", '', compressed_file_name)

                compressed_original_file_name = file_name + ".pdf"

                # Check if the original file name matches the compressed file name
                if compressed_original_file_name == original_file_path:
                    # Check if compressed and original file exists
                    logging_replace = f"Replace: \t{compressed_file_path}\nto: \t\t{original_file_path}"
                    if os.path.exists(Path(original_file_path).resolve()) and os.path.exists(Path(compressed_file_path).resolve()):
                        print(logging_replace)
                        shutil.move(Path(compressed_file_path), Path(original_file_path))
                    else:
                        output_errors += f"\n\033[91mFile Replacing Error\033[0m\n{logging_replace}\n"

    # If there are any errors, print them at once
    if len(output_errors) > 0:
        print("\n\033[91mFILES THAT COULDN'T BE REPLACED BY THE SCRIPT HAVE TO BE MANUALLY REPLACED\033[0m")
        print(output_errors)


if __name__ == "__main__":
    main()
