# !/usr/bin/env python3

"""
file_operation.py

Module for performing various file operations including reading, writing, renaming, and converting files.

Description:
This module provides a collection of methods for performing various operations on files. It includes methods for reading and writing text files,
validating file paths, converting Word documents to PDF, and renaming files in a folder. The module utilizes the `tkinter` library for GUI
functionality to prompt the user to select files or folders, the `pandas` library for reading CSV files, the `docx2pdf` library for converting Word
documents to PDF, and the `os` library for file and directory operations. The `FileOperation` class is the main class in this module,
which encapsulates all the file operation methods. The `main()` function is provided for standalone execution, which initiates the file operations
and prints "done" upon completion.
"""

import os
from datetime import datetime
from pathlib import Path
from shutil import copytree
from tkinter import filedialog, Tk

import pandas as pd
from docx2pdf import convert
from docxtpl import DocxTemplate
from eglogging import logging_load_human_config

from PDF_Operation.pdf_operation import PdfOperation
from Text_Operation.text_operation import TextOperation

logging_load_human_config()


class FileOperation:
    def __init__(self):
        """
        Initializes the FileOperation class with no parameters.
        """
        # No need to initialize anything
        self.text_ops = TextOperation(text="")
        self.pdf_ops = PdfOperation()

    @staticmethod
    def get_current_folder_path():
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return current_dir

    def get_parent_folder_path(self):
        current_dir = self.get_current_folder_path()
        # Go up one level
        parent_dir = os.path.dirname(current_dir)
        return parent_dir

    @staticmethod
    def copy_folder_structure(input_folder=None):
        """
        Copies a selected folder structure and appends the current date and time to the copied folder's name.
        Args:
            input_folder (str): The path to the folder to be copied.
        """
        if input_folder is None:
            folder1 = filedialog.askdirectory()
            if not folder1:
                raise SystemExit("No input folder selected.")
        else:
            folder1 = input_folder

        # folder path with time of now
        now = datetime.now().strftime("%Y.%m.%d %H.%M")
        folder2 = f'{folder1} {now}'

        # Create the new folder structure
        for folder_path, folder_names, filenames in os.walk(folder1):
            structure = folder_path.replace(folder1, folder2)
            if not os.path.isdir(structure):
                os.makedirs(structure)

        print(f"Input: {folder1}")
        print(f"Output: {folder2}")
        return folder1, folder2

    @staticmethod
    def copy_folder_and_files(input_folder=None):
        """
        Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.
        Args:
            input_folder (str): The path to the folder to be copied.
        """
        if input_folder is None:
            folder1 = filedialog.askdirectory()
            if not folder1:
                raise SystemExit("No input folder selected.")
        else:
            folder1 = input_folder

        # folder path with time of now
        now = datetime.now().strftime("%Y.%m.%d %H.%M")
        folder2 = f'{folder1} {now}'

        # copy folder
        copytree(folder1, folder2)

        print(f"Input: {folder1}")
        print(f"Output: {folder2}")
        return folder1, folder2

    def create_folders_in_folder(self, folder, text):
        """
        Creates a new folder with a specified name within a given folder.
        Args:
            folder (str): The path to the folder where the new folder will be created.
            text (str): The name of the new folder.
        """
        self.text_ops.text = text
        folder_name = self.text_ops.clean_string()
        if not folder_name:
            raise SystemExit
        folder_path = os.path.join(folder, folder_name)
        os.makedirs(folder_path)
        print(f"Output: {folder_name}")

    @staticmethod
    def select_folder_word_csv():
        """
        Prompts the user to select a folder to save populated Word documents, a Word template file, and a CSV file containing data.
        Returns:
            tuple: The paths of the selected folder, Word template file, and CSV file.
        """
        # Prompt user to select a folder to save populated Word documents
        folder = filedialog.askdirectory()
        if not folder:
            return None, None, None

        # Prompt user to select Word template file
        template_file = filedialog.askopenfilename(filetypes=[("Word Files", ".docx .doc")])
        if not template_file:
            return None, None, None

        # Prompt user to select CSV file containing data
        csv_file = filedialog.askopenfilename(filetypes=[("Excel Files", ".xlsx .xls .csv")])
        if not csv_file:
            return None, None, None

        if not all([folder, template_file, csv_file]):
            raise SystemExit("No input file selected.")
        else:
            print("Folder: ", folder)
            print("Template File: ", template_file)
            print("CSV File: ", csv_file)

        return folder, template_file, csv_file

    def csv_populate_word(self, filename_placeholder, list_of_placeholders):
        """
        Populates a Word template document with data from a CSV file, replacing placeholders in the template with values from each row of the CSV.
        Args:
            filename_placeholder (str): The placeholder in the Word template to be replaced with the filename.
            list_of_placeholders (list): A list of placeholders in the Word template to be replaced with values from the CSV file.
        """
        # Select files
        folder, template_file, csv_file = self.select_folder_word_csv()
        # Read CSV file into DataFrame
        dataframe = pd.read_csv(csv_file)

        # Iterate through each row in the CSV file
        for index, row in dataframe.iterrows():
            # Create context dictionary with placeholder values from current row
            context = {filename_placeholder: row[filename_placeholder]}
            for value in list_of_placeholders:
                context[value] = row[value]

            # Load Word template
            docx = DocxTemplate(template_file)

            # Populate template with context and save
            docx.render(context)
            file_name = f"{folder}/{row[filename_placeholder]}.docx"
            docx.save(file_name)
            print(f"Created Word document: {file_name}")

    @staticmethod
    def is_filepath_valid(filename, allowed_paths):
        """
        Validates a file path to prevent traversal attacks.
        Args:
            filename (str): The absolute path to the file.
            allowed_paths (list): A list of paths to directories where files can be accessed.
        Returns:
            bool: True if the file path is valid, False otherwise.
        """
        # Normalize and get absolute path
        filename = os.path.abspath(os.path.normpath(filename))

        # Check if file path starts with any of the allowed paths
        for path in allowed_paths:
            if filename.startswith(os.path.abspath(os.path.normpath(path))) and not filename.startswith(".."):
                return True
        return False

    def read_write_txt(self, filename, text_input, allowed_paths):
        """
        Reads a text file, appends a specified text to it, and writes the result back to the file.
        If the file does not exist, it creates the file.
        Args:
            filename (str): The absolute path to the text file.
            text_input (str): The text to be appended to the file.
            allowed_paths (list): The path to the directory where files can be written.
        """
        # function that read & write .txt file
        root = Tk()
        root.withdraw()

        # Validate and sanitize the filename
        if not self.is_filepath_valid(filename, allowed_paths):
            raise ValueError("Filepath is not accessible.")

        # Check if file exists, if not, create it
        if not os.path.exists(filename):
            open(filename, 'w').close()

        # Read & write file
        with open(filename, 'r+', encoding='utf-8') as file:
            file.write(str(text_input))

        # Read the latest file
        with open(filename, 'r', encoding='utf-8') as file:
            open(filename, 'r').close()

        return file

    # def word_to_pdf_in_folder(self):
    #     """
    #     Converts all Word documents in a specified folder to PDF format.
    #     """
    #     root = Tk()
    #     root.withdraw()
    #     folder1, folder2 = self.copy_folder_structure()
    #     convert(folder1, folder2)
    #     for root, dirs, files in os.walk(folder1):
    #         for directory in dirs:
    #             print(root)
    #             print(files)
    #             folder_path1 = os.path.join(root, directory)
    #             folder_path2 = folder_path1.replace(folder1, folder2)
    #             convert(folder_path1, folder_path2)
    #             print("\n")

    def word_to_pdf_in_folder(self):
        """
        Converts all Word documents in a specified folder to PDF format.
        """
        root = Tk()
        root.withdraw()
        folder1, folder2 = self.copy_folder_structure()
        convert(folder1, folder2)
        for root, dirs, files in os.walk(folder1):
            for directory in dirs:
                print(directory)
                print(files)
                folder_path1 = os.path.join(root, directory)
                folder_path2 = folder_path1.replace(folder1, folder2)
                convert(folder_path1, folder_path2)
                print("\n")

    def rename_file_in_folder(self, args):
        """
        Renames all files in a specified folder based on the provided arguments.
        This method iterates over each file in the specified folder, and for each file, it performs a series of operations
        defined by the arguments. These operations can include adding a title from the file, removing a prefix, adding a prefix or suffix,
        and changing the case of the filename. The method uses an instance of the TextOperation class to perform these operations.
        After the operations are performed, the file is renamed with the new filename.
        Args:
            args (argparse.Namespace): The parsed command line arguments. These arguments define the operations to be performed on the filenames
        Note:
            This method creates a new TextOperation object for each file, and deletes it after the file is renamed. This is done to minimize memory
            usage.
        """
        counter = 1
        folder = Path(args.input)

        # Get the list of files once and iterate over it
        for entry in os.scandir(folder):
            if entry.is_file():
                # Create a new TextOperation object for each file
                text_ops = TextOperation(text="")
                text_ops.set_args(args)

                # Get the full file path once and reuse it
                file_path = Path(entry.path)
                full_filename = Path(entry.name)

                if text_ops.add_title == 1:
                    # Todo: detect for file type and create functions to get title from word/excel/text
                    filename1 = self.pdf_ops.extract_title_from_pdf(file_path, title_keyword="Title")
                else:
                    filename1 = os.path.splitext(full_filename)[0]

                extension = full_filename.suffix.lower()

                # Reset the text attribute for each file
                text_ops.text = filename1

                filename2 = text_ops.process_text(counter)
                file2 = folder / f"{filename2}{extension}"

                # rename file parsed in
                print(file2)
                file_path.rename(file2)
                counter += 1

                # Delete the TextOperation object to free up memory
                del text_ops

        # print(args)
        # print(text_ops)
        # print(text_ops.text)
        # print(text_ops.add_title)
        # print(text_ops.title_keyword)
        # print(text_ops.prefix_operation)
        # print(text_ops.suffix_operation )
        # print(text_ops.case_operation)
        # print(text_ops.prefix)
        # print(text_ops.suffix)
        # print(text_ops.remove_prefix)
        # print(text_ops.prefix_delimiter)
        # print(text_ops.page_text)
