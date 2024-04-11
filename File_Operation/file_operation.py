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

# !/usr/bin/env python3
import os
from datetime import datetime
from shutil import copytree
from tkinter import filedialog, Tk

import pandas as pd
from docx2pdf import convert
from docxtpl import DocxTemplate
from eglogging import logging_load_human_config

from PDF_Operation.pdf_operation import PdfOperation
from Text_Operation.text_operation import TextOperation
from config import file_show_folder_dialog

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
    def copy_folder(input_folder):
        """
        Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.
        Args:
            input_folder (str): The path to the folder to be copied.
        """
        if file_show_folder_dialog:
            folder1 = filedialog.askdirectory()
            if not folder1:
                raise SystemExit("No input folder selected.")
        else:
            folder1 = input_folder

        # folder path with time of now
        now = datetime.now().strftime("%Y.%m.%d %H.%M")
        folder2 = f'{folder1} {now}'

        # Create the new folder structure
        for dirpath, dirnames, filenames in os.walk(folder1):
            structure = os.path.join(folder2, dirpath[len(folder1):])
            if not os.path.isdir(structure):
                os.mkdir(structure)

        print(folder1)
        print(folder2)
        return folder1, folder2

    @staticmethod
    def copy_folder_and_files(input_folder):
        """
        Copies a selected folder along with all its contents and appends the current date and time to the copied folder's name.
        Args:
            input_folder (str): The path to the folder to be copied.
        """
        if file_show_folder_dialog:
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

        print(folder1)
        print(folder2)
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
        print(f"Created folder '{folder_name}'.")

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

    def is_filepath_valid(self, filename, allowed_paths):
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

    @staticmethod
    def word_to_pdf_in_folder(folder):
        """
        Converts all Word documents in a specified folder to PDF format.
        Args:
            folder (str): The path to the folder containing the Word documents to be converted.
        """
        root = Tk()
        root.withdraw()
        folder1, folder2 = FileOperation.copy_folder(folder)
        convert(folder1, folder2)

    def rename_file_in_folder(self, folder):
        """
        Renames all files in a specified folder according to a certain pattern.
        Args:
            folder (str): The path to the folder containing the files to be renamed.
        """
        counter = 1

        # iterate all the files in the folder & rename file
        for count, file in enumerate(os.listdir(folder)):
            # file 1 properties
            file1 = os.path.join(folder, file)
            full_filename = os.path.split(file1)[1]

            if self.text_ops.to_get_title_from_file == 1:
                # detect for file type 
                # and create functions to get title from word/excel/text in the future 
                filename1 = self.pdf_ops.get_title_from_pdf(file1, keyword="Title")
            else:
                filename1 = os.path.splitext(full_filename)[0]
            extension = os.path.splitext(full_filename)[1].lower()

            # get prefix or suffix
            self.text_ops.prefix = self.text_ops.get_prefix(counter)
            self.text_ops.suffix = self.text_ops.get_suffix(counter)

            # file 2 properties
            self.text_ops.text = filename1
            filename2 = self.text_ops.remove_prefix()
            filename2 = f"{self.text_ops.prefix}{filename2}{self.text_ops.suffix}"
            self.text_ops.text = filename2
            filename2 = self.text_ops.change_case()
            file2 = os.path.join(folder, f"{filename2}{extension}")

            # rename file parsed in
            print(file2)
            os.rename(file1, file2)
            counter += 1
