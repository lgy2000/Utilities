# !/usr/bin/env python3

"""
count_file_size_by_type_in_folder.py

This module is used for counting the file size by type in a folder.

Description:
This module iterates over all files in a specified folder, categorizing them by file type and summing up the total size for each type. The results
are then printed to the console.
"""

import collections
import os


def count_file_size_by_type_in_folder(directory):
    # Initialize a dictionary to store the counts and sizes
    file_extension_counts = collections.defaultdict(int)
    file_extension_sizes = collections.defaultdict(int)
    total_counts = 0
    total_size = 0

    # Walk through the directory recursively
    for dirpath, dirnames, filenames in os.walk(directory):
        # For each file, get the extension and increment its count
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            file_extension_counts[extension] += 1
            file_extension_sizes[extension] += file_size

    # Print the counts and sizes
    for extension, count in file_extension_counts.items():
        size = file_extension_sizes[extension] / 1024 / 1024
        print(f"{extension}:\t{count} files,\t{int(size)} MB")
        total_counts += count
        total_size += size

    print(f"\nTotal files: {total_counts}\nTotal size: {int(total_size)} MB")


def main():
    directory = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\___WP126 PU\2.0 Engineering - Copy\RevF1\New folder\2"
    count_file_size_by_type_in_folder(directory)


if __name__ == '__main__':
    main()
