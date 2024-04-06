from tkinter import filedialog

from PyPDF2 import PdfReader, PdfWriter

from config import rotation_angle, show_file_dialog, input_file


def rotate_pdf_page(angle, reader, writer):
    # Rotate each page and add it to the output PDF
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        page.rotate(angle)
        writer.add_page(page)


def rotate_pdf_pages(rotation_angle):
    if show_file_dialog == 1:
        file = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
    else:
        file = input_file
    # Open the input PDF file
    with open(file, 'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()

        rotate_pdf_page(rotation_angle, reader, writer)

        # Write the rotated pages to the output PDF file
        with open(file, 'wb') as output_pdf:
            writer.write(output_pdf)


def main():
    rotate_pdf_pages(rotation_angle)
    print('done')


if __name__ == '__main__':
    main()
