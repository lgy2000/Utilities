"""
Module name: word_to_pdf_in_folder.py

Description:
Converts all Word files within a specified folder into PDF files and saves them in the same or another folder.

Notes:
- The module relies on the `tkinter` library for GUI functionality to prompt the user to select a folder.
- It also utilizes the `docx2pdf` library for Word to PDF conversion.
- The `word_to_pdf_in_folder()` function prompts the user to select a folder via a GUI dialog if `show_folder_dialog` is enabled, otherwise it uses
the `input_folder` specified in the configuration.
- It then converts all Word files in the selected folder into PDF files and saves them in the same folder.
- The `main()` function initiates the Word to PDF conversion process and prints "done" upon completion.
- Note: The `word_to_pdf_in_folder()` function is called twice unnecessarily at the end of the module and can be removed.
"""

from file_operation import FileOperation


def main():
    file_ops = FileOperation()
    file_ops.word_to_pdf_in_folder()
    print('done')


if __name__ == '__main__':
    main()
