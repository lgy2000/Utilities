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

from config import filename, list_of_placeholders
from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    file_ops.csv_populate_word(filename, list_of_placeholders)


if __name__ == '__main__':
    main()
