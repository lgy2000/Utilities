"""
Module name: create_folder_in_folder.py

Description:
Creates folders within a specified directory based on user input. Each folder name is entered interactively via the console, and folders are
created inside the specified directory.

Notes:

The module allows users to input folder names interactively via the console until they press Enter to finish.
The script utilizes the os module for file system operations and the tkinter module for GUI functionality to prompt the user to select the
directory where folders will be created.
Upon execution, the main() function prompts the user to select a directory using a GUI dialog. If a directory is selected, the create_folders()
function is called to create folders within that directory based on user input.
If no directory is selected, the script prints "No folder selected." and terminates.
The user can terminate the folder creation process by entering 'Q' during the folder name input prompt, which raises a SystemExit exception.
"""

import os
from tkinter import filedialog


def create_folders(folder):
    print("Enter folder names (press Enter to finish):")
    while True:
        folder_name = input().strip()
        if folder_name.upper() == 'Q':
            raise SystemExit
        if not folder_name:
            break  # Stop input loop if Enter is pressed
        try:
            folder_path = os.path.join(folder, folder_name)
            os.makedirs(folder_path)
            print(f"Created folder '{folder_name}'.")
        except OSError as e:
            print(f"Error: {e}")


def main():
    folder = filedialog.askdirectory()
    if folder:
        create_folders(folder)
    else:
        print("No folder selected.")


if __name__ == "__main__":
    main()
