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

from kindle_operation import KindleOperation

from config import file_input_folder
from file_operation import FileOperation
import argparse
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from PDF_Operation.pdf_operation import PdfOperation
from config import file_show_file_dialog, pdf_input_file

logging_load_human_config()


def parse_command_line_args():
    """
    Parses the command line arguments passed to the script.
    Returns:
        argparse.Namespace: The parsed command line arguments, which include the input HTML file,
        whether to include the location of notes/highlights, whether to export the output to the clipboard or a file,
        and whether to override an existing output file.
    """
    description = "Convert an HTML file of book notes exported from an Amazon " \
                  "Kindle to a Markdown document"
    parser = argparse.ArgumentParser(description=description)

    base_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script

    # positional input argument
    parser.add_argument('input',
                        nargs='?',  # makes the input argument optional
                        default=os.path.join(base_dir, ".test", "example_notebook.html"),  # default value if no input argument is provided
                        help='Input HTML file')

    parser.add_argument('-nl', '--no-location',
                        dest='location',
                        action='store_false',
                        default=True,
                        help='Whether to skip export of location of notes/highlights')

    parser.add_argument('-c', '--clipboard',
                        action='store_true',
                        help='Whether to export .md directly to the clipboard instead of file')

    parser.add_argument('-y', '--override',
                        action='store_true',
                        default=False,
                        help='Whether to override .md file in case if one already exists')

    parser.add_argument('-o', '--output',
                        default='',
                        help='Change markdown document filepath')

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
        'location': "Whether to skip export of location of notes/highlights? (yes/no) ",
        'clipboard': "Whether to export .md directly to the clipboard instead of a file? (yes/no) ",
        'override': "Whether to override .md file in case if one already exists? (yes/no) "
    }

    # Get the input file from the user
    arguments.input = filedialog.askopenfilename(filetypes=[("HTML Files", ".html")])
    if not arguments.input:
        raise SystemExit("No input file selected.")

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
                    setattr(arguments, attr, bool_map[user_input])  # Set the attribute based on the user input
                    break  # Break the loop as a valid input is provided
                else:
                    print("Invalid input. Please try again.")

    # Handle the 'output' attribute separately
    while True:
        user_input = input("Change markdown document filepath (filepath/no) ").lower()
        # if no output passed, output .md file next to original HTML notes
        if os.path.splitext(user_input)[1] == '.md':
            setattr(arguments, 'output', user_input)  # Set the attribute based on the user input
            break  # Break the loop as a valid input is provided
        elif user_input in ['no', '']:
            break


def main():
    try:
        file_ops = FileOperation()
        args = parse_command_line_args()
        # if no arguments are provided from the system terminal, get user input from the console
        if len(sys.argv) == 1:
            get_user_input(args)
        _, folder2 = file_ops.copy_folder_and_files(file_input_folder)
        file_ops.rename_file_in_folder(folder2)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
