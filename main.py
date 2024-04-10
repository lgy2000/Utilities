import ast
import os
import subprocess

from tabulate import tabulate

# Input
project_folder = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
exclude_folders = ["test", "youtube_transcript_api"]
file_custom_input = ["modify_text.py"]


def get_callable_functions(file_path, cache=None):
    """Detect callable functions in a Python file."""
    if cache is None:
        cache = {}

    if file_path in cache:
        return cache[file_path]

    try:
        if file_path.endswith('.py'):
            with open(file_path, 'r', encoding='utf-8') as file:
                tree = ast.parse(file.read(), filename=file_path)

            callable_functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            cache[file_path] = callable_functions
            return callable_functions

    except UnicodeDecodeError as e:
        print(f"Unicode Decode Error: {e} for file: {file_path}")
    except Exception as e:
        print(f"Error: {e} for file: {file_path}")

    return None


def list_python_files(_project_folder, _exclude_folders):
    """List Python files excluding specified folders."""
    all_files_list = []
    num = 0
    for (current_path, dir_names, file_names) in os.walk(_project_folder):
        if not any(exclude_folder in current_path for exclude_folder in _exclude_folders):
            for file_name in sorted(file_names):
                if file_name.endswith('.py'):
                    file_object = []
                    num += 1
                    file_path = os.path.join(current_path, file_name)
                    callable_functions = get_callable_functions(file_path)

                    file_object.append(num)
                    file_object.append(current_path)
                    file_object.append(file_name)
                    file_object.append(callable_functions)
                    all_files_list.append(file_object)

    return all_files_list


def execute_script(file_path, custom_input=None):
    """Execute Python script with optional custom input."""
    if custom_input is not None:
        subprocess.run(["python", file_path, custom_input])
    else:
        subprocess.run(["python", file_path])


def main_menu():
    all_files_list = list_python_files(project_folder, exclude_folders)
    print("\n", tabulate(all_files_list, headers=["NO", "PATH", "FILE", "FUNCTIONS"]))

    print("\nInput the file number to execute a python script, or type \"folder\" to open folder location")
    user_input = input("Action: ")

    if user_input.isdigit():
        file_num_input = int(user_input) - int(1)
        file_path_input = all_files_list[file_num_input][1]
        file_name_input = all_files_list[file_num_input][2]

        if file_name_input in file_custom_input:
            custom_input = input(f"Enter custom input for {file_name_input}: ")
            execute_script(os.path.join(file_path_input, file_name_input), custom_input)
        else:
            execute_script(os.path.join(file_path_input, file_name_input))
    if str(user_input).lower() == "folder":
        subprocess.Popen(f'explorer /select, {project_folder}')

    again()


def again():
    print("\n")
    again_input = input("Press M (Main Menu) or Blank (Quit): ")
    if again_input.upper() == 'M':
        main_menu()
    elif not again_input.upper():
        raise SystemExit
    else:
        again()


def main():
    print("Welcome to this cool utility!")
    main_menu()


if __name__ == '__main__':
    main()
