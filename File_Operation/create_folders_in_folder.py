"""
create_folders_in_folder.py

Creates multiple folders within a specified directory.

Description:
This module provides a function to create multiple folders within a specified directory. The names of the folders to be created are read from a
text file. It utilizes the os module for directory and file operations.
"""

from tkinter import filedialog

from file_operation import FileOperation


def main():
    print("Enter folder names: ")
    try:
        file_ops = FileOperation()
        folder = filedialog.askdirectory()
        if not folder:
            raise SystemExit("No input folder selected.")
        folder_names = []
        while True:
            line = input()
            if line:
                folder_names.append(line)
            else:
                break
        if folder_names:
            for folder_name in folder_names:
                file_ops.create_folders_in_folder(folder, folder_name)
        else:
            print("No folder selected.")
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
