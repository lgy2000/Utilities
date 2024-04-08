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

from eglogging import *

from kindle_operation import KindleNotes

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

    # positional input argument
    parser.add_argument('input',
                        nargs='?',  # makes the input argument optional
                        default=r'D:\YK\Python\Utilities\Kindle_Operation\.test\example_notebook.html',  # default value if no input argument is
                        # provided
                        help='Input HTML file')

    parser.add_argument('-nl', '--no-location',
                        dest='location',
                        action='store_false',
                        default=True,
                        help='Whether to skip export of location of notes/highlights')

    parser.add_argument('-c', '--clipboard',
                        action='store_true',
                        help='Use to export .md directly to the clipboard instead of file')

    parser.add_argument('-y', '--override',
                        action='store_true',
                        default=False,
                        help='Whether to override .md file in case if one already exists')

    parser.add_argument('-o', '--output',
                        default='',
                        help='A file to which save the Markdown document')

    arguments = parser.parse_args()

    # if no output passed, output .md file next to original HTML notes
    arguments.output = os.path.splitext(arguments.input)[0] + '.md'

    return arguments


if __name__ == '__main__':
    """
    Main entry point of the script. It parses the command line arguments,
    reads the input HTML file, converts it to Markdown format, and writes
    the output to a file or clipboard based on the arguments.
    """
    try:
        args = parse_command_line_args()

        notes = KindleNotes()
        notes.parse_file(args.input)
        notes.output_md(args)
        input("Press any key to exit")

    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)
