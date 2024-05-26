# !/usr/bin/env python3

"""
delete_empty_folders_in_folder_with_rename_index.py

This module is used for deleting empty directories and renaming the remaining directories in a specified path.

Description:
This module contains a function that iterates over all items in a specified directory. If an item is a directory and it is empty,
the module removes it. After deleting empty directories, it renames the remaining directories by adding an index before their names.
"""

import os
import re

from natsort import natsorted


def delete_empty_folders_and_rename(path):
    # Iterate over all items in the directory
    for item in os.scandir(path):
        # If the item is a directory
        if item.is_dir():
            # If the directory is empty
            if len(os.listdir(item.path)) == 0:
                # Remove the directory
                os.rmdir(item.path)
                print(f"Deleted empty directory: {item.path}")

    # Get the list of remaining directories and sort them
    remaining_dirs = natsorted([d for d in os.scandir(path) if d.is_dir()], key=lambda d: d.name)

    # Iterate over the sorted list of directories and rename them
    for i, dir in enumerate(remaining_dirs, start=1):
        old_name = dir.name
        # Remove leading number from the old name
        new_name = re.sub(r'^\d+\s*', '', old_name)
        # Form the new name with the index and the old name
        new_name = f"{i} {new_name}"
        # Rename the directory
        os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
        print(f"Renamed directory: {old_name} -> {new_name}")


def main():
    path = r"D:\YK\Downloads\hui - Copy - Copy"  # Replace with your directory path
    delete_empty_folders_and_rename(path)


if __name__ == "__main__":
    main()
