# !/usr/bin/env python3

"""
copy_folder_and_files.py

Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.

Description:
This module provides a function to copy a selected folder along with all its contents. The copied folder's name is appended with the current date
and time. It utilizes the datetime, shutil, and tkinter modules for date-time manipulation, file copying, and GUI functionality respectively.
"""

import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

from config import file_input_folder
from file_operation import FileOperation

logging_load_human_config()


def main():
    try:
        file_ops = FileOperation()
        file_ops.copy_folder_and_files(file_input_folder)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
