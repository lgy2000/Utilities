# !/usr/bin/env python3

"""
list_files_in_folders_excel.py

This module is used for listing all files in a directory into a CSV file.

Description:
This module contains a function that iterates over all files in a specified directory and writes their full path, file name, and extension into a
CSV file. The CSV file is saved in the same directory.
"""

import os

import pandas as pd


def list_files_to_excel(folder_path, excel_file_path):
    data = []
    for file_name in os.listdir(folder_path):
        full_file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(full_file_path):  # Ensure it's a file, not a directory
            file_name_without_ext, extension = os.path.splitext(file_name)
            data.append([file_name_without_ext, extension, full_file_path])
        elif os.path.isdir(full_file_path):  # If it's a directory
            data.append([file_name, "", full_file_path])

    df = pd.DataFrame(data, columns=["Name", "Extension", "Full File Path"])
    df.to_excel(excel_file_path, index=False)


if __name__ == "__main__":
    folder_path = r"D:\YK\Downloads\Book"  # replace with your folder path
    excel_file_path = folder_path + r"\_Summary.xlsx"  # replace with your Excel file path
    list_files_to_excel(folder_path, excel_file_path)
