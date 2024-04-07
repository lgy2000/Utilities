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

from datetime import datetime
from shutil import copytree
from tkinter import filedialog

from config import file_show_folder_dialog, file_input_folder


def copy_folder(input_folder):
    """copy the folder and its contents"""
    if file_show_folder_dialog:
        folder1 = filedialog.askdirectory()
    else:
        folder1 = input_folder

    # copy folder with time of now
    now = datetime.now().strftime("%Y.%m.%d %H.%M")

    folder2 = f'{folder1} {now}'
    copytree(folder1, folder2)

    print(folder1)
    print(folder2)
    return folder1, folder2


def main():
    copy_folder(file_input_folder)
    print("done")


if __name__ == "__main__":
    main()
