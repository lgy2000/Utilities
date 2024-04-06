"""
copy_folder.py

Description:
Copy the selected folder with all files in it and append the date and time on the folder's name'

Notes:

"""

from datetime import datetime
from shutil import copytree
from tkinter import filedialog

from config import show_folder_dialog, input_folder


def copy_folder():
    """copy the folder and its contents"""
    if show_folder_dialog:
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
    copy_folder()
    print("done")


if __name__ == "__main__":
    main()
