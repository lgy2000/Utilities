"""
file_operation.py

Provides various file operations such as copying folders, populating Word documents with CSV data, and converting Word documents to PDF.

Description:
This module defines a class that provides various file operations. These operations include copying folders, populating Word documents with CSV
data, renaming files in a folder, and converting Word documents to PDF. It utilizes the os, pandas, docx, and tkinter modules for directory and
file operations, data manipulation, Word document operations, and GUI functionality respectively.
"""

import os
from datetime import datetime
from shutil import copytree
from tkinter import filedialog, Tk

import pandas as pd
from docx2pdf import convert
from docxtpl import DocxTemplate

from File_Operation.text_operation import TextOperation
from PDF_Operation.pdf_operation import PdfOperation
from config import file_show_folder_dialog, file_input_folder


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

        # copy folder with time of now
        now = datetime.now().strftime("%Y.%m.%d %H.%M")

        folder2 = f'{folder1} {now}'
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
        try:
            folder_path = os.path.join(folder, folder_name)
            os.makedirs(folder_path)
            print(f"Created folder '{folder_name}'.")
        except OSError as e:
            print(f"Error: {e}")

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
        try:
            dataframe = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        # Iterate through each row in the CSV file
        for index, row in dataframe.iterrows():
            # Create context dictionary with placeholder values from current row
            context = {filename_placeholder: row[filename_placeholder]}
            for value in list_of_placeholders:
                context[value] = row[value]

            # Load Word template
            docx = DocxTemplate(template_file)

            # Populate template with context and save
            try:
                docx.render(context)
                file_name = f"{folder}/{row[filename_placeholder]}.docx"
                docx.save(file_name)
                print(f"Created populated Word document: {file_name}")
            except Exception as e:
                print(f"Error populating Word document: {e}")

    @staticmethod
    def read_write_txt(text_input):
        """
        Reads a text file, appends a specified text to it, and writes the result back to the file.
        Args:
            text_input (str): The text to be appended to the file.
        """
        # function that read & write .docx file
        root = Tk()
        root.withdraw()
        filename = filedialog.askopenfilename()
        if not filename:
            raise SystemExit("No input file selected.")

        # Read & write file
        file = open(filename, 'r+', encoding='utf-8')
        file.write(str(text_input))
        file.close()

        # Read the latest file
        file = open(filename, 'r', encoding='utf-8')
        file.close()

    @staticmethod
    def word_to_pdf_in_folder():
        """
        Converts all Word documents in a selected folder to PDF format.
        """
        root = Tk()
        root.withdraw()
        if file_show_folder_dialog == 1:
            folder = filedialog.askdirectory()
            if not folder:
                raise SystemExit("No input folder selected.")
        else:
            folder = file_input_folder
        convert(folder, folder)

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
