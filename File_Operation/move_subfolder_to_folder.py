# !/usr/bin/env python3

"""
move_subfolder_to_folder.py

This module is used for moving all files from a subfolder to its parent folder.

Description:
This module contains a function that iterates over all files in a specified subfolder and moves them to the parent directory. If the subfolder is
empty after the move, it is removed.
"""

import os
import shutil
from tkinter import filedialog


# TODO: move function to file_operations.py


def move_subfolder_to_folder(directory, subfolder_name='subfolder_'):
    # List all subdirectories in the given directory
    subfolders = [f.path for f in os.scandir(directory) if f.is_dir()]
    for subfolder in subfolders:
        # Check if the subfolder's name starts with the given prefix
        if os.path.basename(subfolder).startswith(subfolder_name):
            print(f"Subfolder: {subfolder}")
            # List all entries (files and folders) in the subfolder
            entries = os.listdir(subfolder)
            for entry in entries:
                src_path = os.path.join(subfolder, entry)
                dst_path = os.path.join(directory, entry)
                print(f"Moving {src_path}")
                # Move each entry to the parent directory
                shutil.move(src_path, dst_path)
            # Remove the subfolder if it's empty
            if not os.listdir(subfolder):
                os.rmdir(subfolder)
            print("\n")


def main():
    folder = filedialog.askdirectory()
    subfolder_name = ''
    move_subfolder_to_folder(folder, subfolder_name)


if __name__ == "__main__":
    main()
