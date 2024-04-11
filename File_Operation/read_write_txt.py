"""
read_write_txt.py

Module for reading and overwriting text files with specified input.

Description:
This module reads the contents of a text file and overwrites it with a specified text input. It utilizes the `tkinter` library for GUI
functionality to prompt the user to select a text file. The `read_write_txt()` function prompts the user to select a text file via a GUI dialog and
overwrites its contents with the specified text input. The input text is provided by the `text_input` argument of the function. The function first
opens the selected file in read-write mode, writes the input text to it, and then closes the file. It then reopens the file in read mode to ensure
that the latest changes are read. The `main()` function is provided for standalone execution, which initiates the text read-write process and
prints "done" upon completion.
"""

# !/usr/bin/env python3
import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

from config import input_text, file_allowed_paths, file_input_file
from file_operation import FileOperation

logging_load_human_config()


def main():
    try:
        file_ops = FileOperation()
        # file_input_file = filedialog.askopenfilename()
        # file_input_file = r'D:\YK\Resources\input.txt'
        if not file_input_file:
            raise SystemExit("No input file selected.")
        file_ops.read_write_txt(file_input_file, input_text, file_allowed_paths)
        print(input_text)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
