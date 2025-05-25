# !/usr/bin/env python3

"""
list_files_in_folders_json.py

This module is used for listing all files in a directory into a JSON file.

Description:
This module contains a function that iterates over all files in a specified directory and writes their full path, file name, and extension into a
JSON file. The JSON file is saved in the same directory.
"""

import os
import json


def list_files_to_json(folder_path, json_file_path):
    data = []
    for file_name in os.listdir(folder_path):
        full_file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(full_file_path):  # Ensure it's a file, not a directory
            file_name_without_ext, extension = os.path.splitext(file_name)
            data.append({
                "name": file_name_without_ext,
                "extension": extension,
                "full_file_path": full_file_path
            })
        elif os.path.isdir(full_file_path):  # If it's a directory
            data.append({
                "name": file_name,
                "extension": "",
                "full_file_path": full_file_path
            })

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    folder_path = r"D:\YK\Python\ObsiGen Framework\data\frameworks"  # replace with your folder path
    json_file_path = folder_path + r"\_Summary.json"  # replace with your JSON file path
    list_files_to_json(folder_path, json_file_path)