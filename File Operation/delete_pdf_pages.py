"""
Module name: delete_pdf_pages.py

Description:
Removes specific pages from all PDF files.

Notes:

The module utilizes the tkinter and pikepdf modules for GUI functionality and PDF manipulation respectively.
The delete_pdf_pages() function prompts the user to select a PDF file via a GUI dialog.
It then removes the page specified by page_number from the selected PDF file.
The modified PDF is saved with a filename appended with " Modified" to distinguish it from the original.
The main() function is provided for standalone execution, which initiates the deletion process and prints "done" upon completion.
"""

from tkinter import filedialog

import pikepdf

from config import page_number


def delete_pdf_pages(page_number):
    """remove specific pages from all PDF files """
    filename1 = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
    filename2 = f'{filename1}'.replace('.pdf', ' Modified.pdf')
    file = pikepdf.Pdf.open(filename1)
    del file.pages[page_number]
    file.save(filename2)


def main():
    delete_pdf_pages(page_number)
    print('done')


if __name__ == '__main__':
    main()
