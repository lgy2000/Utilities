"""
copy_folder.py

Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.

Description:
This module provides a function to copy a selected folder along with all its contents. The copied folder's name is appended with the current date
and time. It utilizes the datetime, shutil, and tkinter modules for date-time manipulation, file copying, and GUI functionality respectively.
"""

from config import file_input_folder
from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    file_ops.copy_folder(file_input_folder)


if __name__ == "__main__":
    main()
