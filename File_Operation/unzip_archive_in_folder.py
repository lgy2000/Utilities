# !/usr/bin/env python3

"""
unzip_archive_in_folder.py

Unzips archive files in a given directory.

Description:
This module contains a function that traverses a given directory and unzips any archive files it encounters. It supports both .zip and .rar file
formats. The unzipped files are placed in the same directory as the original archive.
"""

# Todo: move function to PDF_Operation folder

import os
import zipfile

import rarfile


def unzip_archives_in_folder(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                print(type(file_path))
                print(type('r'))
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
            elif file.endswith('.rar'):
                file_path = os.path.join(root, file)
                with rarfile.RarFile(file_path, 'r') as rar_ref:
                    rar_ref.extractall(root)


def main():
    unzip_archives_in_folder(r"D:\YK\Downloads\TRANSMITTAL2")


if __name__ == "__main__":
    main()
