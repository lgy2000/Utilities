# Utilities

This project consists of a collection of utility scripts and modules, organized into different directories based on their functionality. Each
directory contains Python scripts that perform specific tasks.

## Directory Structure

The project is organized into the following directories:

- `Data_Operation`
- `Email_Operation`
- `File_Operation`
- `Kindle_Operation`
- `PDF_Operation`

### Data_Operation (to-do list)

This directory contains modules and scripts related to data operations.

### Email_Operation

This directory contains modules and scripts related to email operations. The following files are included:

- `email_operation.py`: Contains a class that includes various operations related to emails.
- `count_email_files.py`: Counts the number of email files.
- `download_email_files.py`: Downloads email files.
- `email_search_error.py`: Handles email search errors.

### File_Operation

This directory contains modules and scripts related to file operations. The following files are included:

- `file_operation.py`: Contains a class that includes various operations related to files.
- `text_operation.py`: Contains a class that includes various operations related to text.
- `copy_folder_and_files.py`: Copies a folder.
- `create_folder_in_folder_in_terminal.py`: Creates a folder within another folder from the terminal.
- `create_folders_in_folder.py`: Creates multiple folders within a folder.
- `csv_populate_word.py`: Populates a Word document with data from a CSV file.
- `modify_text.py`: Modifies text in a file.
- `read_write_txt.py`: Reads and writes to a text file.
- `rename_file.py`: Renames a file.
- `word_to-pdf-in_folder.py`: Converts Word documents to PDF in a folder.

### Kindle_Operation

This directory contains modules and scripts related to Kindle operations. The following files are included:

- `kindleoperation.py`: Contains a class that includes various operations related to Kindle.
- `kindle_notes_html_to_md.py`: Converts Kindle notes from HTML to Markdown.
- `kindle_notes_html-to-md_screenshot.png`: A screenshot showing the conversion of Kindle notes from HTML to Markdown.

### PDF_Operation

This directory contains modules and scripts related to PDF operations. The following files are included:

- `pdf_operation.py`: Contains a class that includes various operations related to PDF files. It includes functions for deleting pages, rotating
  pages, extracting text from a
  PDF file, checking if a string is present in a PDF file, and extracting a title from a PDF file. It uses the PyPDF2 and pikepdf libraries for PDF
  file
  operations.
- `delete_pdf_pages.py`: Deletes specific pages from a PDF file.
- `delete_pdf_pages_in_folder.py`: Deletes specific pages from all PDF files within a folder.
- `extract_title_from_pdf.py`: Extracts the title from a PDF file.
- `pdf_operation_test.py`: Contains tests for the pdf_operation.py module.
- `rotate_pdf.py`: Rotates each page in a PDF file by a specified angle.
- `rotate_pdf-in_folder.py`: Rotates each page in all PDF files within a folder by a specified angle.

## Usage

Each script can be run independently or run from the `main_menu.py`. Please refer to the individual script files for specific usage instructions.

## Current To-do List

- Add more comments and docstrings in the classes and modules `File_Operation`.
- Add more functionality and instructions in the main menu.
- Enable the user to input arguments in the main menu.
- Retest all the scripts and modules.