# !/usr/bin/env python3

"""
extract_page_from_pdf_contain_keywords.py

Extract pages from a PDF file that contain specified keywords.

Description:
This module contains a function that reads a PDF file and checks each page for the presence of specified keywords. Pages that do not contain any of
the keywords are deleted. The remaining pages are written to a new PDF file.
"""

# Todo: move function to PDF_Operation folder

from PyPDF2 import PdfReader, PdfWriter

from extract_text_from_pdf import extract_text_from_pdf


def extract_page_from_pdf_contain_keywords(file_path, keywords, output_path):
    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PdfReader(file)

        # Initialize a PDF writer object
        pdf_writer = PdfWriter()

        # Loop through each page in the PDF file
        for page in pdf_reader.pages:
            # Extract the text from the current page
            text = page.extract_text()

            # Check if any of the keywords are in the text of the current page
            if any(keyword in text for keyword in keywords):
                # If a keyword is found, add the page to the PDF writer object
                pdf_writer.add_page(page)

        # Write the PDF writer object to a new PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    # Return the new PDF file
    return output_path


def main():
    keyword_file_path = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_LOGIC DIAGRAM\RESET-EXE-HES-93-INC-DWG-4214_0 Cropped.pdf"
    input_pdf_path = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_LOGIC DIAGRAM\RESET-EXE-HES-93-INC-DWG-4214_F2 Hard Copy.pdf"
    output_pdf_path = (r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_LOGIC DIAGRAM\RESET-EXE-HES-93-INC-DWG-4214_F2 Hard "
                       r"Copy2.pdf")
    keywords = extract_text_from_pdf(keyword_file_path)
    new_file = extract_page_from_pdf_contain_keywords(input_pdf_path, keywords, output_pdf_path)
    print(f"New PDF file with pages containing keywords: {new_file}")


if __name__ == "__main__":
    main()
