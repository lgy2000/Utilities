"""
Module name: rename_file_in_folder.py

Description:
Renames all files within a specified folder according to configured patterns and modifications.

Notes:
- The module depends on the `os` module for file system operations and imports functionalities from other modules (`config.py`, `copy_folder.py`,
`get_title_from_pdf.py`, `modify_text.py`).
- The `rename_file_in_folder()` function prompts the user to input keyword, delimiter, prefix, and suffix if configured, and then iterates through
all files in the specified folder to rename them accordingly.
- If configured, it extracts titles from files using the specified keyword using functionality from the `get_title_from_pdf.py` module.
- Prefixes and suffixes are added to filenames based on the configured options, and case modifications are applied as specified.
- The `main()` function initiates the process by copying files from one folder to another using functionality from the `copy_folder.py` module,
and then calls the `rename_file_in_folder()` function to rename files in the copied folder.
"""

import os

from PDF_Operation.pdf_operation import PdfOperation
from config import file_input_folder, to_add_title, to_remove_prefix, to_add_prefix, to_add_suffix, to_change_case
from copy_folder import copy_folder
from modify_text import remove_prefix, add_prefix, add_suffix, change_case

pdf_ops = PdfOperation()


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
            filename1 = pdf_ops.get_title_from_pdf(file1, keyword)
        else:
            filename1 = os.path.splitext(full_filename)[0]
        extension = os.path.splitext(full_filename)[1].lower()

        # get prefix or suffix
        prefix = add_prefix(to_add_prefix, file1, counter, prefix_str)
        suffix = add_suffix(to_add_suffix, file1, counter, suffix_str)

        # file 2 properties
        filename2 = remove_prefix(filename1, delimiter)
        filename2 = f"{prefix}{filename2}{suffix}"
        filename2 = change_case(to_change_case, filename2)
        file2 = os.path.join(folder, f"{filename2}{extension}")

        # rename file parsed in
        print(file2)
        os.rename(file1, file2)
        counter += 1


def main():
    _, folder2 = copy_folder(file_input_folder)
    rename_file_in_folder(folder2)
    print("done")


if __name__ == '__main__':
    main()
