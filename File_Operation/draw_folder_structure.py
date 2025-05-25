# !/usr/bin/env python3

"""
draw_folder_structure.py

Draws the structure of a specified folder.

Description:
This module provides a function to draw the structure of a specified folder. It prints the folder structure to the console, with indentation
indicating subfolders. It utilizes the os module for directory operations.
"""

import ast
import os
import sys
import traceback
from tkinter import filedialog

from eglogging import logging_load_human_config, CRITICAL

from file_operation import FileOperation

logging_load_human_config()


def get_callable_functions(filepath, cache=None):
    """
    Detects and returns the names of callable functions in a Python file.
    Args:
        filepath (str): The path to the Python file to be parsed.
        cache (dict, optional): A cache to store previously parsed files. Defaults to None.
    Returns:
        list: A list of callable function names in the Python file.
    """
    if cache is None:
        cache = {}

    if filepath in cache:
        return cache[filepath]

    try:
        if filepath.endswith('.py'):
            with open(filepath, 'r', encoding='utf-8') as file:
                # Parse the Python file into an AST
                tree = ast.parse(file.read(), filename=filepath)

            # Extract the names of all function definitions in the AST
            callable_functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            cache[filepath] = callable_functions
            return callable_functions

    except UnicodeDecodeError as e:
        print(f"Unicode Decode Error: {e} for file: {filepath}")
    except Exception as e:
        print(f"Error: {e} for file: {filepath}")

    return None


def calculate_indent(level, is_dir=True):
    """
    Calculates the indentation based on the level of depth in the directory structure.
    Args:
        level (int): The level of depth in the directory structure.
        is_dir (bool, optional): A flag indicating whether the current item is a directory. Defaults to True.
    Returns:
        str: The indentation string.
    """
    if level > 0:
        indent = '│   ' * (level - 1) + '├───' if is_dir else '│   ' * level
    else:
        indent = ''
    return indent


def print_with_indent(name, indent, file):
    """
    Prints a name with the specified indentation to the console and writes it to a file.
    Args:
        name (str): The name to be printed.
        indent (str): The indentation string.
        file (file): The file to write the name and indentation to.
    """
    print('{}{}'.format(indent, name))
    file.write('{}{}\n'.format(indent, name))


def print_callable_functions(filepath, indent, file):
    """
    Prints the callable functions in a Python file with the specified indentation to the console and writes them to a file.
    Args:
        filepath (str): The path to the Python file.
        indent (str): The indentation string.
        file (file): The file to write the callable functions and indentation to.
    """
    callable_functions = get_callable_functions(filepath)
    if callable_functions:
        print('{}{}'.format(indent + '    ', callable_functions))
        file.write('{}{}\n'.format(indent + '    ', callable_functions))


def draw_directory_structure(folder, exclude_folders, file):
    """
    Draws the structure of a specified folder, excluding certain subfolders, and writes it to a file.
    Args:
        folder (str): The path to the folder.
        exclude_folders (list): A list of subfolder names to exclude.
        file (file): The file to write the directory structure to.
    """
    for root, dirs, files in os.walk(folder):
        if any(exclude_folder in root for exclude_folder in exclude_folders):
            continue
        level = root.replace(folder, '').count(os.sep)
        indent = calculate_indent(level)
        new_line_indent = calculate_indent(level, is_dir=False)
        print('{}'.format(new_line_indent))
        file.write('{}\n'.format(new_line_indent))
        print_with_indent(os.path.basename(root), indent, file)
        sub_indent = calculate_indent(level, is_dir=False)
        if dirs:
            sub_indent += '│   '
        else:
            sub_indent += '    '
        for f in files:
            print_with_indent(f, sub_indent, file)
            if f.endswith('.py'):
                print_callable_functions(os.path.join(root, f), sub_indent, file)


def main():
    """
    Main function to execute the script. It prompts the user for a directory path, checks if the path exists, and draws the directory structure.
    """
    try:
        # Ask the user for the directory path
        folder = filedialog.askdirectory()
        # Check if the path exists, otherwise use a default path
        if not os.path.exists(folder):
            file_ops = FileOperation()
            folder = file_ops.get_parent_folder_path()
        print(folder)

        # Define the folders to exclude
        exclude_folders = ["__pycache__", ".temp", ".idea", ".git", ".test", "youtube_transcript_api", "webpack", "dist"]
        # Draw the directory structure
        md_file = os.path.join(folder, 'project_structure.md')
        with open(md_file, 'w', encoding='utf-8') as file:
            # Draw the directory structure
            file.write('```')
            draw_directory_structure(folder, exclude_folders, file)
            file.write('```')
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
