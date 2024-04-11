"""
csv_populate_word.py

Populates a Word template document with data from a CSV file.

Description:
This module provides a function to populate a Word template document with data from a CSV file. It replaces placeholders in the template with
values from each row of the CSV. It utilizes the pandas and docx modules for data manipulation and Word document operations respectively.
"""

from config import filename, list_of_placeholders
from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    file_ops.csv_populate_word(filename, list_of_placeholders)


if __name__ == '__main__':
    main()
