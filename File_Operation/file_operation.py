import os
from datetime import datetime
from shutil import copytree
from tkinter import filedialog

import pandas as pd
from docxtpl import DocxTemplate

from config import file_show_folder_dialog
from text_operation import TextOperation


class FileOperation:
    def __init__(self):
        # No need to initialize anything
        self.text_ops = TextOperation()

    @staticmethod
    def copy_folder(input_folder):
        """copy the folder and its contents"""
        if file_show_folder_dialog:
            folder1 = filedialog.askdirectory()
        else:
            folder1 = input_folder

        # copy folder with time of now
        now = datetime.now().strftime("%Y.%m.%d %H.%M")

        folder2 = f'{folder1} {now}'
        copytree(folder1, folder2)

        print(folder1)
        print(folder2)
        return folder1, folder2

    def create_folders_in_folder(self, folder):
        print("Enter folder names (press Enter to finish):")
        while True:

            folder_name = self.text_ops.clean_string(input())
            if folder_name.upper() == 'Q':
                raise SystemExit
            if not folder_name:
                break  # Stop input loop if Enter is pressed
            try:
                folder_path = os.path.join(folder, folder_name)
                os.makedirs(folder_path)
                print(f"Created folder '{folder_name}'.")
            except OSError as e:
                print(f"Error: {e}")

    def select_folder_word_csv(self):
        """
        Prompts the user to select a folder to save populated Word documents,
        a Word template file, and a CSV file containing data.
        Returns the paths of the selected files.
        """
        # Prompt user to select a folder to save populated Word documents
        folder = filedialog.askdirectory()
        if not folder:
            print("No folder selected.")
            return None, None, None

        # Prompt user to select Word template file
        template_file = filedialog.askopenfilename(filetypes=[("Word Files", ".docx .doc")])
        if not template_file:
            print("No Word template file selected.")
            return None, None, None

        # Prompt user to select CSV file containing data
        csv_file = filedialog.askopenfilename(filetypes=[("Excel Files", ".xlsx .xls .csv")])
        if not csv_file:
            print("No CSV file selected.")
            return None, None, None

        return folder, template_file, csv_file

    def csv_populate_word(self, filename, list_of_placeholders):
        """
        Populates a Word template document with data from a CSV file, replacing placeholders
        in the template with values from each row of the CSV.
        """
        # Select files
        folder, template_file, csv_file = self.select_folder_word_csv()
        if not all((folder, template_file, csv_file)):
            return

        # Read CSV file into DataFrame
        try:
            dataframe = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        # Iterate through each row in the CSV file
        for index, row in dataframe.iterrows():
            # Create context dictionary with placeholder values from current row
            context = {filename: row[filename]}
            for value in list_of_placeholders:
                context[value] = row[value]

            # Load Word template
            docx = DocxTemplate(template_file)

            # Populate template with context and save
            try:
                docx.render(context)
                file_name = f"{folder}/{row[filename]}.docx"
                docx.save(file_name)
                print(f"Created populated Word document: {file_name}")
            except Exception as e:
                print(f"Error populating Word document: {e}")

        print("done")
