"""
Module name: csv_populate_word.py

Description:
Populates a Word template document with data from a CSV file, replacing placeholders in the template with values from each row of the CSV.

Notes:

The module utilizes the tkinter, pandas, and docxtpl modules for GUI functionality, CSV file handling, and Word document templating respectively.
The csv_populate_word() function prompts the user to select a folder to save the populated Word documents, a Word template file (.docx or .doc),
and a CSV file containing data.
It iterates through each row in the CSV file, replacing placeholders in the Word template with corresponding values from each row.
Placeholders and their corresponding values are defined by the filename and list_of_placeholders variables respectively, sourced from the config.py
file.
The populated Word documents are saved in the selected folder with filenames derived from the value in the specified filename column of the CSV.
The main() function is provided for standalone execution, which initiates the population process and prints "done" upon completion.
"""
from tkinter import filedialog
import pandas as pd
from docxtpl import DocxTemplate
from config import filename, list_of_placeholders


def select_files():
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


def populate_word_from_csv():
    """
    Populates a Word template document with data from a CSV file, replacing placeholders
    in the template with values from each row of the CSV.
    """
    # Select files
    folder, template_file, csv_file = select_files()
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


def main():
    populate_word_from_csv()


if __name__ == '__main__':
    main()
