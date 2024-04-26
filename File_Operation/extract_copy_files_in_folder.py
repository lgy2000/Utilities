# !/usr/bin/env python3

"""
extract_copy_files_in_folder.py

Extracts and copies files with specified keywords in a directory to a destination directory.

Description:
This module contains a function that traverses a given directory and copies any files whose names contain specified keywords to a destination
directory. The function returns a list of the file paths that were copied.
"""

# Todo: move function to FileOperation

import fnmatch
import os
import shutil


def extract_files_with_keywords(directory, keywords, destination_directory):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for keyword in keywords:
                if fnmatch.fnmatch(file, f'*{keyword}*'):
                    source_file_path = os.path.join(root, file)
                    matching_files.append(source_file_path)
                    print(source_file_path)
                    shutil.copy2(source_file_path, str(destination_directory))
    return matching_files


def main():
    keywords = ["DWG-4223"]
    directory = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\Transmittal Outgoing 2024.4.25"
    destination_directory = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_HMI PRINTOUT OMS"
    extract_files_with_keywords(directory, keywords, destination_directory)


if __name__ == "__main__":
    main()
