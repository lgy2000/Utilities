"""
draw_folder_structure.py

Draws the structure of a specified folder.

Description:
This module provides a function to draw the structure of a specified folder. It prints the folder structure to the console, with indentation
indicating subfolders. It utilizes the os module for directory operations.
"""

import ast
import os


def get_callable_functions(filepath, cache=None):
    """
    Detect callable functions in a Python file.
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
    if level > 0:
        indent = '│   ' * (level - 1) + '├───' if is_dir else '│   ' * level
    else:
        indent = ''
    return indent


def print_with_indent(name, indent, file):
    print('{}{}'.format(indent, name))
    file.write('{}{}\n'.format(indent, name))


def print_callable_functions(filepath, indent, file):
    callable_functions = get_callable_functions(filepath)
    if callable_functions:
        print('{}{}'.format(indent + '    ', callable_functions))
        file.write('{}{}\n'.format(indent + '    ', callable_functions))


def draw_directory_structure(folder, exclude_folders, file):
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
    Main function to execute the script.
    """
    # Ask the user for the directory path
    print("Enter the directory path: ")
    folder = input()
    # Check if the path exists, otherwise use a default path
    folder = folder if os.path.exists(folder) else r"D:\YK\Python\Utilities"
    # Define the folders to exclude
    exclude_folders = ["__pycache__", ".temp", ".idea", ".git", ".test", "youtube_transcript_api"]
    # Draw the directory structure
    md_file = os.path.join(folder, 'project_structure.md')
    with open(md_file, 'w', encoding='utf-8') as file:
        # Draw the directory structure
        file.write('```')
        draw_directory_structure(folder, exclude_folders, file)
        file.write('```')


if __name__ == '__main__':
    main()
