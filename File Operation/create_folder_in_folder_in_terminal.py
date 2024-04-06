"""
Module name: create_folder_in_folder_in_terminal.py

Description:
Creates folders within a specified directory based on user input. Each folder name is entered interactively via the terminal, and folders are
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
import sys

def create_folders(folder, folder_names):
    for folder_name in folder_names:
        if not folder_name:
            continue  # Skip empty lines
        try:
            folder_path = os.path.join(folder, folder_name)
            os.makedirs(folder_path)
            print(f"Successfully created folder '{folder_name}'.")
        except OSError as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python create_folders.py <folder_path> <folder_name1> <folder_name2> ...")
        sys.exit(1)

    folder = sys.argv[1]
    folder_names = sys.argv[2:]
    create_folders(folder, folder_names)

if __name__ == "__main__":
    main()
