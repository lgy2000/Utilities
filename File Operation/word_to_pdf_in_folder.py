import ctypes
from tkinter import *
from tkinter import filedialog

from docx2pdf import convert

from config import show_folder_dialog, input_folder


def word_to_pdf_in_folder():
    """convert all the Word files in the folder into PDF files and save in another folder"""
    root = Tk()
    root.withdraw()
    if show_folder_dialog == 1:
        folder = filedialog.askdirectory()
    else:
        folder = input_folder
    convert(folder, folder)


def main():
    word_to_pdf_in_folder()
    print('done')


if __name__ == '__main__':
    main()

word_to_pdf_in_folder()
