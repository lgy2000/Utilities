# !/usr/bin/env python3

"""
docstring_manager.py

This module is used for managing docstrings in Python files.

Description:
This module scans all Python files in a specified directory and checks if they have a docstring. It prints the file paths of those files that do
not have a docstring.
"""

import ast
import os
from tkinter import filedialog


# TODO: move function to file_operations.py

def has_docstring(filename):
    with open(filename, "r", encoding='utf-8') as source:
        tree = ast.parse(source.read())
        return ast.get_docstring(tree) is not None


def main():
    directory = filedialog.askdirectory()
    print("Files that do not have a docstring:")
    # Scan all files in a directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a Python file
            if file.endswith('.py'):
                # Check if the file has a docstring
                file_path = os.path.join(root, file)
                if not has_docstring(file_path):
                    print(f"{file_path}")


if __name__ == "__main__":
    main()
