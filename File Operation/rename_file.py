"""
rename_file.py

Description:
Rename all files in a folder according to the user's preference'

Notes:
- Input values for the configuration variables.

"""

import os

from config import to_add_title, to_remove_prefix, to_add_prefix, to_add_suffix
from copy_folder import copy_folder
from get_title_from_file import get_title_from_file
from modify_text import remove_prefix, add_prefix, add_suffix, change_case


def rename_file_in_folder(folder):
    """rename all the files in the folder with a pattern"""
    # Get values from copy_folder()

    counter = 1
    keyword = input("Input keyword: ") if to_add_title == 1 else ""
    delimiter = input("Input delimiter: ") if to_remove_prefix == 1 else ""
    prefix_str = input("Input prefix: ") if to_add_prefix == 3 else ""
    suffix_str = input("Input suffix: ") if to_add_suffix == 3 else ""

    # iterate all the files in the folder & rename file
    for count, file in enumerate(os.listdir(folder)):
        # file 1 properties
        file1 = os.path.join(folder, file)
        full_filename = os.path.split(file1)[1]

        if to_add_title == 1:
            filename1 = get_title_from_file(file1, keyword)
        else:
            filename1 = os.path.splitext(full_filename)[0]
        extension = os.path.splitext(full_filename)[1].lower()

        # get prefix or suffix
        prefix = add_prefix(file1, counter, prefix_str)
        suffix = add_suffix(file1, counter, suffix_str)

        # file 2 properties
        filename2 = remove_prefix(filename1, delimiter)
        filename2 = f"{prefix}{filename2}{suffix}"
        filename2 = change_case(filename2)
        file2 = os.path.join(folder, f"{filename2}{extension}")

        # rename file parsed in
        print(file2)
        os.rename(file1, file2)
        counter += 1


def main():
    folder1, folder2 = copy_folder()
    rename_file_in_folder(folder2)
    print("done")


if __name__ == '__main__':
    main()
