# !/usr/bin/env python3

"""
find_old_pdf.py

This module is used for finding old PDF files in a selected folder.

Description:
This module asks the user to select a folder, and then finds all PDF files in the selected folder that are older than a specified period. The paths
of the old files are returned.
"""

import os
import time
from tkinter import filedialog


def main(folder):
    # Define the period in seconds
    period_days = 2

    # Get the current time
    current_time = time.time()

    old_file_path = []

    # Walk through the directory to find all PDF files
    for path, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(path, file)
                # Get the time of the last modification of the file
                file_time = os.path.getmtime(file_path)
                duration = (current_time - file_time) / 24 / 60 / 60
                # Check if the file is older than the period
                if duration > period_days:
                    print(f"{int(duration)} days:\t{file_path}")
                    old_file_path.append(file_path)

    return old_file_path


if __name__ == "__main__":
    folder_ = filedialog.askdirectory()
    main(folder_)
