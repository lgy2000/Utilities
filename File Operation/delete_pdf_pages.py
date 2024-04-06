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
