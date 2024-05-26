# !/usr/bin/env python3

"""
rename_files_in_folder.py

This module is used for renaming all files within a specified folder according to configured patterns and modifications.

Description:
This module provides functionality to rename all files in a given folder based on user-specified patterns and modifications. It includes options to
add or remove prefixes and suffixes, change case, and extract titles from files. The module uses the `os` module for file system operations and
imports functionalities from other modules.
"""

import argparse
import gc
import os
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from Text_Operation.text_operation import TextOperationArgs
from file_operation import FileOperation

logging_load_human_config()


def get_test_folder():
    """
    Get the test file path.
    Returns:
        str: The test file path.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
    test_folder = os.path.join(base_dir, r".test\test1")
    return test_folder


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
        folder = filedialog.askdirectory()
        args = TextOperationArgs(input=folder, add_title=False, title_keyword="", prefix_operation="", suffix_operation="",
                                 case_operation="UPPER", prefix="", suffix="", remove_prefix=False, prefix_delimiter="")
        file_ops = FileOperation()

        _, folder = file_ops.copy_folder_and_files(args.input)
        args.input = folder  # If no folder is provided, open a file dialog to select a folder
        file_ops.rename_file_in_folder(args)

        # Call gc.collect() to free up memory immediately
        gc.collect()
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
