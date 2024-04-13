"""
Module name: rename_file_in_folder.py

Description:
Renames all files within a specified folder according to configured patterns and modifications.

Notes:
- The module depends on the `os` module for file system operations and imports functionalities from other modules (`config.py`,
`copy_folder_and_files.py`,
`get_title_from_pdf.py`, `modify_text.py`).
- The `rename_file_in_folder()` function prompts the user to input keyword, delimiter, prefix, and suffix if configured, and then iterates through
all files in the specified folder to rename them accordingly.
- If configured, it extracts titles from files using the specified keyword using functionality from the `get_title_from_pdf.py` module.
- Prefixes and suffixes are added to filenames based on the configured options, and case modifications are applied as specified.
- The `main()` function initiates the process by copying files from one folder to another using functionality from the `copy_folder_and_files.py`
module,
and then calls the `rename_file_in_folder()` function to rename files in the copied folder.
"""

# !/usr/bin/env python3
import argparse
import os
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from file_operation import FileOperation

logging_load_human_config()


def get_test_folder():
    """
    Get the test file path.
    Returns:
        str: The test file path.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
    test_folder = os.path.join(base_dir, r".test\test")
    return test_folder


def parse_command_line_args():
    """
    Parses the command line arguments passed to the script.
    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    description = "Renames all files within a specified folder " \
                  "according to configured patterns and modifications."
    parser = argparse.ArgumentParser(description=description)

    test_folder = get_test_folder()

    # positional input argument
    parser.add_argument('input',
                        nargs='?',  # makes the input argument optional
                        default=test_folder,  # default value if no input argument is provided
                        help='Input folder path')

    parser.add_argument('--to-add-title-from-file',
                        action='store_true',
                        help='Whether to add title from file')

    parser.add_argument('--to-remove-prefix',
                        action='store_true',
                        help='Whether to remove prefix')

    parser.add_argument('--to-add-prefix',
                        action='store_true',
                        help='Whether to add prefix')

    parser.add_argument('--to-add-suffix',
                        action='store_true',
                        help='Whether to add suffix')

    parser.add_argument('--to-change-case',
                        action='store_true',
                        help='Whether to change case')

    parser.add_argument('--keyword',
                        default='',
                        help='Keyword to use if to_get_title_from_file is set')

    parser.add_argument('--prefix-delimiter',
                        default='',
                        help='Prefix delimiter to use if to_remove_prefix is set')

    parser.add_argument('--prefix-str',
                        default='',
                        help='Prefix string to use if to_add_prefix is set')

    parser.add_argument('--suffix-str',
                        default='',
                        help='Suffix string to use if to_add_suffix is set')

    arguments = parser.parse_args()

    return arguments


def get_user_input(arguments):
    """
    Prompts the user for input if no arguments are provided from the system terminal.
    Args:
        arguments (argparse.Namespace): The parsed command line arguments.
    Returns:
        None
    """
    # Define a dictionary to store the prompts and corresponding attribute names
    configurations = {
        'to-get-title-from-file': "Whether to get title from file? (yes/no) ",
        'to-remove-prefix': "Whether to remove prefix? (yes/no) ",
        'to-add-prefix': "Whether to add prefix? (yes/no) ",
        'to-add-suffix': "Whether to add suffix? (yes/no) ",
        'to-change-case': "Whether to change case? (yes/no) ",
        'keyword': "Keyword to use if to_get_title_from_file is set: ",
        'prefix-delimiter': "Prefix delimiter to use if to_remove_prefix is set: ",
        'prefix-str': "Prefix string to use if to_add_prefix is set: ",
        'suffix-str': "Suffix string to use if to_add_suffix is set: "
    }

    # Get the input folder from the user
    arguments.input = filedialog.askdirectory()
    if not arguments.input:
        test_folder = get_test_folder()
        setattr(arguments, 'input', test_folder)

    # Ask the user if they want to skip other configurations
    print("Press enter to skip other configurations or any other key to continue: ")
    other_args = input()
    # If the user didn't press enter, ask for the other configurations
    if other_args:
        for attr, prompt in configurations.items():
            while True:  # Loop until a valid input is provided
                user_input = input(prompt).lower()
                if user_input in ['yes', 'no', '']:
                    bool_map = {'yes': True, 'no': False, '': False}
                    if attr in ['to-get-title-from-file', 'to-remove-prefix', 'to-add-prefix', 'to-add-suffix', 'to-change-case']:
                        setattr(arguments, attr, bool_map[user_input])  # Set the attribute based on the user input
                    else:
                        setattr(arguments, attr, user_input if user_input else None)
                    break  # Break the loop as a valid input is provided
                else:
                    print("Invalid input. Please try again.")


def main():
    try:
        file_ops = FileOperation()
        args = parse_command_line_args()
        # if no arguments are provided from the system terminal, get user input from the console
        if len(sys.argv) == 1:
            get_user_input(args)

        print(f"{args.input} is processed.")
        _, folder = file_ops.copy_folder_and_files(args.input)
        args.input = folder
        file_ops.rename_file_in_folder(args)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
