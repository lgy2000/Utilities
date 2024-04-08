"""
Module name: create_folders_in_folder.py

Description:
Creates folders within a specified directory based on user input. Each folder name is entered interactively via the console, and folders are
created inside the specified directory.

Notes:

The module allows users to input folder names interactively via the console until they press Enter to finish.
The script utilizes the os module for file system operations and the tkinter module for GUI functionality to prompt the user to select the
directory where folders will be created.
Upon execution, the main() function prompts the user to select a directory using a GUI dialog. If a directory is selected,
the create_folders_in_folder()
function is called to create folders within that directory based on user input.
If no directory is selected, the script prints "No folder selected." and terminates.
The user can terminate the folder creation process by entering 'Q' during the folder name input prompt, which raises a SystemExit exception.
"""

from tkinter import filedialog

from file_operation import FileOperation


def main():
    try:
        file_ops = FileOperation()
        folder = filedialog.askdirectory()

        if folder:
            file_ops.create_folders_in_folder(folder)
        else:
            print("No folder selected.")
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
