# !/usr/bin/env python3

"""
list_file_in_csv.py

This module is used for listing all files in a directory into a CSV file.

Description:
This module contains a function that iterates over all files in a specified directory and writes their full path, file name, and extension into a
CSV file. The CSV file is saved in the same directory.
"""

import csv
import os


def list_files_to_csv(folder_path, csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Full File Path", "File Name", "Extension"])
        for file_name in os.listdir(folder_path):
            full_file_path = os.path.join(folder_path, file_name)
            file_name_without_ext, extension = os.path.splitext(file_name)
            writer.writerow([full_file_path, file_name_without_ext, extension])


if __name__ == "__main__":
    folder_path = r"E:"  # replace with your folder path
    csv_file_path = folder_path + r"\Summary.csv"  # replace with your CSV file path
    list_files_to_csv(folder_path, csv_file_path)
