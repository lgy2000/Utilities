# !/usr/bin/env python3

"""
rename_file_in_folder.py

Renames all files within a specified folder according to configured patterns and modifications.

Description:
This module provides functionality to rename all files in a given folder based on user-specified patterns and modifications. It includes options to
add or remove prefixes and suffixes, change case, and extract titles from files. The module uses the `os` module for file system operations and
imports functionalities from other modules (`config.py`, `copy_folder_and_files.py`, `extract_title_from_pdf.py`, `modify_text.py`). The main function
initiates the process by copying files from one folder to another and then calls the `rename_file_in_folder()` function to rename files in the
copied folder.
"""

import argparse
import gc
import os
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from Text_Operation.text_operation import TextOperation, Prefix, Suffix, Case
from file_operation import FileOperation

logging_load_human_config()


# TODO: case operation not working

def get_test_folder():
    """
    Get the test file path.
    Returns:
        str: The test file path.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
    test_folder = os.path.join(base_dir, r".test\test1")
    return test_folder


def to_uppercase(value: str) -> str:
    return value.upper()


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
    parser.add_argument('--add_title',
                        action='store_true',
                        help='Whether to add title from file')
    parser.add_argument('--title_keyword',
                        default='',
                        help='Keyword to use if to_get_title_from_file is set')
    parser.add_argument('--prefix_operation',
                        choices=[prefix.name for prefix in Prefix],
                        type=to_uppercase,
                        default=Prefix.NONE.name,
                        help='Prefix operation to perform')
    parser.add_argument('--suffix_operation',
                        choices=[suffix.name for suffix in Suffix],
                        type=to_uppercase,
                        default=Suffix.NONE.name,
                        help='Suffix operation to perform')
    parser.add_argument('--case_operation',
                        choices=[case.name for case in Case],
                        type=to_uppercase,
                        default=Case.NONE.name,
                        help='Case operation to perform')
    parser.add_argument('--prefix',
                        default='',
                        help='Prefix string to use if to_add_prefix is set')
    parser.add_argument('--suffix',
                        default='',
                        help='Suffix string to use if to_add_suffix is set')
    parser.add_argument('--remove_prefix',
                        action='store_true',
                        help='Whether to remove prefix')
    parser.add_argument('--prefix_delimiter',
                        default=' ',
                        help='Prefix delimiter to use if _remove_prefix is set')

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
        'add_title': "Whether to add title from file? (yes/no) ",
        'title_keyword': "Keyword to use if add_title is set: ",
        'prefix_operation': "Prefix operation to perform (none/counter/timestamp/custom): ",
        'suffix_operation': "Suffix operation to perform (none/counter/timestamp/custom): ",
        'case_operation': "Case operation to perform (none/title/upper/lower): ",
        'prefix': "Prefix string to use if to_add_prefix is set (str): ",
        'suffix': "Suffix string to use if to_add_suffix is set (str): ",
        'remove_prefix': "Whether to remove prefix? (yes/no) ",
        'prefix_delimiter': "Prefix delimiter to use if _remove_prefix is set (str): "
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
                if attr in ['add_title', 'remove_prefix']:
                    bool_map = {'yes': True, 'no': False, '': False}
                    if user_input in bool_map:
                        setattr(arguments, attr, bool_map[user_input])  # Set the attribute based on the user input
                        break  # Break the loop as a valid input is provided
                    else:
                        print("Invalid input. Please try again.")
                elif attr in ['prefix_operation', 'suffix_operation', 'case_operation']:
                    valid_operations = ['none', 'counter', 'timestamp', 'custom'] if attr in ['prefix_operation',
                                                                                              'suffix_operation'] else ['none',
                                                                                                                        'title',
                                                                                                                        'upper',
                                                                                                                        'lower']
                    if user_input in valid_operations:
                        setattr(arguments, attr, user_input.upper() if user_input else None)
                        break  # Break the loop as a valid input is provided
                    else:
                        print("Invalid input. Please try again.")
                else:
                    setattr(arguments, attr, user_input if user_input else None)
                    break  # Break the loop as a valid input is provided


def main():
    try:
        file_ops = FileOperation()
        text_ops = TextOperation(text="")  # create an instance of TextOperation
        file_ops.text_ops = text_ops  # assign the instance to the text_ops attribute of file_ops

        args = parse_command_line_args()
        # if no arguments are provided from the system terminal, get user input from the console
        if len(sys.argv) == 1:
            get_user_input(args)

        _, folder = file_ops.copy_folder_and_files(args.input)  # If no folder is provided, open a file dialog to select a folder
        args.input = folder
        file_ops.rename_file_in_folder(args)

        # Call gc.collect() to free up memory immediately
        gc.collect()
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
