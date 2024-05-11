"""
Module name: rename_file_in_folder.py

Description:
Renames all files within a specified folder according to configured patterns and modifications.

Notes:
- The module depends on the `os` module for file system operations and imports functionalities from other modules (`config.py`, `copy_folder.py`,
`get_title_from_pdf.py`, `modify_text.py`).
- The `rename_file_in_folder()` function prompts the user to input keyword, delimiter, prefix, and suffix if configured, and then iterates through
all files in the specified folder to rename them accordingly.
- If configured, it extracts titles from files using the specified keyword using functionality from the `get_title_from_pdf.py` module.
- Prefixes and suffixes are added to filenames based on the configured options, and case modifications are applied as specified.
- The `main()` function initiates the process by copying files from one folder to another using functionality from the `copy_folder.py` module,
and then calls the `rename_file_in_folder()` function to rename files in the copied folder.
"""

from config import file_input_folder
from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    _, folder2 = file_ops.copy_folder(file_input_folder)
    file_ops.rename_file_in_folder(folder2)


if __name__ == '__main__':
    main()
