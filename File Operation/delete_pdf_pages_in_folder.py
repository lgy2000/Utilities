import os

import pikepdf

from config import page_number
from copy_folder import copy_folder


def delete_pdf_pages_in_folder(page_number, folder):
    """remove specific pages from all PDF files within a folder"""
    for count, filename in enumerate(os.listdir(folder)):
        filename1 = f'{folder}/{filename}'
        file = pikepdf.Pdf.open(filename1)
        del file.pages[page_number]
        filename2 = f'{folder}/{filename}'
        print(filename2)
        file.save(filename2)


def main():
    folder1, folder2 = copy_folder()
    delete_pdf_pages_in_folder(page_number, folder2)
    print('done')


if __name__ == '__main__':
    main()
