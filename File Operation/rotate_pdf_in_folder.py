import os

from PyPDF2 import PdfReader, PdfWriter

from config import rotation_angle
from copy_folder import copy_folder
from rotate_pdf import rotate_pdf_page


def rotate_pdf_pages_in_folder(folder, angle):
    # Iterate over each PDF file in the input directory
    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            file = os.path.join(folder, filename)

            # Open the input PDF file
            with open(file, 'rb') as f:
                reader = PdfReader(f)
                writer = PdfWriter()

                rotate_pdf_page(angle, reader, writer)

                # Write the rotated pages to the output PDF file
                with open(file, 'wb') as output_pdf:
                    writer.write(output_pdf)


def main():
    folder1, folder2 = copy_folder()
    rotate_pdf_pages_in_folder(folder2, rotation_angle)
    print('done')


if __name__ == '__main__':
    main()
