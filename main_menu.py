import ast
import os
import subprocess

from tabulate import tabulate


def detect_callable_functions(file_path):
    """detect callable functions in a file"""
    try:
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read(), filename=file_path)

        callable_functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return callable_functions

    except Exception as e:
        print(f"Error: {e}")
        return None


def main_menu():
    # folder path
    dir_path = r"D:\YK\Python\Utilities"

    # list to store files name
    all_files_list = []
    num = 0

    # detect callable functions in all files in a folder
    for (current_path, dir_names, file_names) in os.walk(dir_path):
        if ".py" in str(file_names) and not ".pyc" in str(file_names):
            print(current_path)
            for file_name in file_names:
                if ".py" in str(file_names) and not ".pyc" in str(file_names):
                    file_object = []
                    num += 1
                    file_path = os.path.join(current_path, file_name)
                    callable_functions = detect_callable_functions(file_path)

                    file_object.append(num)
                    file_object.append(current_path)
                    file_object.append(file_name)
                    file_object.append(callable_functions)
                    all_files_list.append(file_object)

    # print the list of files and its callable functions
    print("\n", tabulate(all_files_list, headers=["NO", "PATH", "FILE", "FUNCTIONS"]), "\n")

    # user select a file in a folder to be executed, or a folder to be opened
    print("Input the file number to execute a python script, or type \"folder\" to open folder location")
    file_folder_input = input("Action: ")
    # user select a file in a folder to be executed
    if str(file_folder_input).lower() != "folder".lower():
        file_num_input = int(file_folder_input) - int(1)
        file_path_input = all_files_list[file_num_input][1]
        file_name_input = all_files_list[file_num_input][2]
        function_input = all_files_list[file_num_input][3]

        file = os.path.join(file_path_input, file_name_input)
        print('\n', file, '\n', function_input)
        subprocess.run(["python", file])


    # user select a folder to be opened
    elif str(file_folder_input).lower() == "folder".lower():
        subprocess.Popen(f'explorer /select, {dir_path}')
    # user did not input a number or "folder"
    else:
        print(f"Please input a number between 1 and {num} or input \"folder\"")

    again()


def again():
    again_input = input('Press M (Main Menu) or Q (Quit): ')
    if again_input.upper() == 'M':
        main_menu()
    elif again_input.upper() == 'Q':
        raise SystemExit
    else:
        again()


main_menu()
