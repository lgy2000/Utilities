# !/usr/bin/env python3

"""
move_folder_to_subfolder_size.py

This module is used for moving folders to subfolders based on a maximum size.

Description:
This module moves folders from a specified directory to newly created subfolders. The total size of the folders in each subfolder does not exceed a
specified maximum size.
"""

import os
import shutil
from tkinter import filedialog


# TODO: move function to file_operations.py

def get_folder_size(folder):
    total = 0
    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            total += os.path.getsize(fp)
    return total


def move_folder_to_subfolder(directory, max_size_mb, subfolder_name='subfolder_'):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    max_size_b = max_size_mb * 1024 * 1024
    total_size = 0
    subfolder_index = 1
    subfolder = os.path.join(directory, f'{subfolder_name}{subfolder_index}')
    os.makedirs(subfolder, exist_ok=True)
    for folder in folders:
        folder_size = get_folder_size(os.path.join(directory, folder))
        if total_size + folder_size > max_size_b:
            subfolder_index += 1
            subfolder = os.path.join(directory, f'{subfolder_name}{subfolder_index}')
            os.makedirs(subfolder, exist_ok=True)
            total_size = 0
        shutil.move(os.path.join(directory, folder), os.path.join(subfolder, folder))
        total_size += folder_size


def main():
    folder = filedialog.askdirectory()
    # Max size per folder
    max_size_mb = 200

    move_folder_to_subfolder(folder, max_size_mb)


if __name__ == "__main__":
    main()
