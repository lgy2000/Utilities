# !/usr/bin/env python3

"""
delete_empty_folders_in_folder.py

This module is used for deleting empty directories in a specified path.

Description:
This module contains a function that iterates over all items in a specified directory. If an item is a directory and it is empty,
the module removes it.
"""

import os


def delete_empty_folders(path):
    # Iterate over all items in the directory
    for item in os.scandir(path):
        # If the item is a directory
        if item.is_dir():
            # If the directory is empty
            if len(os.listdir(item.path)) == 0:
                # Remove the directory
                os.rmdir(item.path)
                print(f"Deleted empty directory: {item.path}")


def main():
    path = r"E:\All\7 Media\7.7 Fitness\Video"  # Replace with your directory path
    delete_empty_folders(path)


if __name__ == "__main__":
    main()
