"""
kindle_notes_html_to_md.py

Converts an HTML file of book notes exported from an Amazon Kindle to a Markdown document.

Description:
This module parses command line arguments, reads the input HTML file, converts it to Markdown format using the KindleNotes class from
kindle_operation module, and writes the output to a file or clipboard based on the arguments.
"""

# !/usr/bin/env python3
import argparse
import os
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from kindle_operation import KindleOperation

logging_load_human_config()


def parse_command_line_args():
    """
    Parse the command line arguments passed to the script.

    Returns:
        argparse.Namespace: The parsed command line arguments.
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
    Get user input for configurations if no arguments are provided from the system terminal.

    Args:
        arguments (argparse.Namespace): The parsed command line arguments.
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
    if other_args != "":
        for attr, prompt in configurations.items():
            while True:  # Loop until a valid input is provided
                user_input = input(prompt).lower()
                if user_input in ['yes', 'no']:
                    bool_map = {'yes': True, 'no': False}
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
        else:
            print("Invalid input. Please try again.")


def main():
    """
    Main entry point of the script. It parses the command line arguments,reads the input HTML file, converts it to Markdown format, and writes the
    output to a file or clipboard based on the arguments.
    """
    try:
        args = parse_command_line_args()
        # if no arguments are provided from the system terminal, get user input from the console
        if len(sys.argv) == 1:
            get_user_input(args)

        print(f"{args.input} is processed.")
        kindle_ops = KindleOperation()
        kindle_ops.parse_file(args.input)
        kindle_ops.output_md(args)
        if len(sys.argv) > 1:
            input("Press any key to exit")
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
