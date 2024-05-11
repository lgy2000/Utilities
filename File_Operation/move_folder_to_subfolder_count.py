# !/usr/bin/env python3

"""
move_folder_to_subfolder_count.py

This module is used for moving files from a folder to subfolders based on a maximum file count.

Description:
This module moves files from a specified folder to newly created subfolders. The number of files in each subfolder does not exceed a specified
maximum count.
"""

import os
import shutil
from math import ceil
from tkinter import filedialog


# TODO: move function to file_operations.py

def move_folder_to_subfolder(directory, max_files, subfolder_name='subfolder_'):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    num_files = len(files)
    if num_files > max_files:
        num_subfolders = ceil(num_files / max_files)
        for i in range(num_subfolders):
            subfolder = os.path.join(directory, f'{subfolder_name}{i + 1}')
            os.makedirs(subfolder, exist_ok=True)
            start = i * max_files
            end = (i + 1) * max_files if (i + 1) * max_files < num_files else num_files
            for j in range(start, end):
                shutil.move(os.path.join(directory, files[j]), os.path.join(subfolder, files[j]))


def main():
    folder = filedialog.askdirectory()
    move_folder_to_subfolder(folder, 10)


if __name__ == "__main__":
    main()
