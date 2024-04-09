import os
from datetime import datetime
from shutil import copytree
from tkinter import filedialog, Tk

import pandas as pd
from docx2pdf import convert
from docxtpl import DocxTemplate

from PDF_Operation.pdf_operation import PdfOperation
from config import file_show_folder_dialog, file_input_folder
from config import to_add_title, to_remove_prefix, to_add_prefix, to_add_suffix, to_change_case
from modify_text import remove_prefix, add_prefix, add_suffix, change_case
from text_operation import TextOperation


class FileOperation:
    def __init__(self):
        # No need to initialize anything
        self.text_ops = TextOperation()
        self.pdf_ops = PdfOperation()

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

    def read_write_txt(self, text_input):
        # function that read & write .docx file
        root = Tk()
        root.withdraw()
        filename = filedialog.askopenfilename()

        # Read & write file
        file = open(filename, 'r+', encoding='utf-8')
        file.write(str(text_input))
        file.close()

        # Read the latest file
        file = open(filename, 'r', encoding='utf-8')
        file.close()

    def word_to_pdf_in_folder(self):
        """convert all the Word files in the folder into PDF files and save in another folder"""
        root = Tk()
        root.withdraw()
        if file_show_folder_dialog == 1:
            folder = filedialog.askdirectory()
        else:
            folder = file_input_folder
        convert(folder, folder)

    def rename_file_in_folder(self, folder):
        """rename all the files in the folder with a pattern"""
        counter = 1
        keyword = input("Input keyword: ") if to_add_title == 1 else ""
        delimiter = input("Input delimiter: ") if to_remove_prefix == 1 else ""
        prefix_str = input("Input prefix: ") if to_add_prefix == 3 else ""
        suffix_str = input("Input suffix: ") if to_add_suffix == 3 else ""

        # iterate all the files in the folder & rename file
        for count, file in enumerate(os.listdir(folder)):
            # file 1 properties
            file1 = os.path.join(folder, file)
            full_filename = os.path.split(file1)[1]

            if to_add_title == 1:
                filename1 = self.pdf_ops.get_title_from_pdf(file1, keyword)
            else:
                filename1 = os.path.splitext(full_filename)[0]
            extension = os.path.splitext(full_filename)[1].lower()

            # get prefix or suffix
            prefix = add_prefix(to_add_prefix, file1, counter, prefix_str)
            suffix = add_suffix(to_add_suffix, file1, counter, suffix_str)

            # file 2 properties
            filename2 = remove_prefix(filename1, delimiter)
            filename2 = f"{prefix}{filename2}{suffix}"
            filename2 = change_case(to_change_case, filename2)
            file2 = os.path.join(folder, f"{filename2}{extension}")

            # rename file parsed in
            print(file2)
            os.rename(file1, file2)
            counter += 1
