"""
create_folders_in_folder.py

Creates multiple folders within a specified directory.

Description:
This module provides a function to create multiple folders within a specified directory. The names of the folders to be created are read from a
text file. It utilizes the os module for directory and file operations.
"""

# !/usr/bin/env python3
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from file_operation import FileOperation

logging_load_human_config()


def main():
    try:
        print("Enter folder names: ")
        file_ops = FileOperation()
        folder = filedialog.askdirectory()
        if not folder:
            raise SystemExit("No input folder selected.")
        folder_names = []
        while True:
            line = input()
            if line:
                folder_names.append(line)
            else:
                break
        if folder_names:
            for folder_name in folder_names:
                file_ops.create_folders_in_folder(folder, folder_name)
        else:
            print("No folder selected.")
    except OSError as e:
        CRITICAL("Exception: {}".format(e))
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
