"""
Module name: copy_folder.py

Description:
Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.

Notes:

The module utilizes the datetime, shutil, and tkinter modules for date-time manipulation, file copying, and GUI functionality respectively.
The copy_folder() function prompts the user to select a folder via a GUI dialog if show_folder_dialog is set to True in the config.py file,
otherwise it uses the input_folder specified in config.py.
It then copies the selected folder along with all its contents to a new folder with the same name appended with the current date and time.
The main() function is provided for standalone execution, which initiates the folder copying process and prints "done" upon completion.
"""

from config import file_input_folder
from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    file_ops.copy_folder(file_input_folder)


if __name__ == "__main__":
    main()
