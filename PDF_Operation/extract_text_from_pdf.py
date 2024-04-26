# !/usr/bin/env python3

"""
extract_text_from_pdf.py

Extracts text from a PDF file.

Description:
This module contains a function that reads a PDF file and extracts all the text from it. The text is returned as a list of strings,
where each string represents the text from a single page of the PDF.
"""

# Todo: move function to PDF_Operation folder

from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text_list = []
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            text = page_text.replace('\n', '').replace(' ', '').split()
            text_list.extend(text)
        return text_list


def is_in_list(list1, list2):
    text_in_list2 = []
    text_not_in_list2 = []
    for element in list1:
        # Check if the current element is a substring in any string in text_list2
        if any(element in item for item in list2):
            text_in_list2.append(element)
        else:
            text_not_in_list2.append(element)

    print(f"Text in list2: {text_in_list2}")
    print(f"Text not in list2: {text_not_in_list2}")


def main():
    file_path = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_LOGIC DIAGRAM\RESET-EXE-HES-93-INC-DWG-4214_0 Cropped.pdf"
    text_list = extract_text_from_pdf(file_path)
    print(f"{text_list}")
    print(f"Total number of words: {len(text_list)}")

    file_path2 = (r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\ASBUILT_DWG_LOGIC DIAGRAM\RESET-EXE-HES-93-INC-DWG-4214_F2 Hard Copy2.pdf")
    text_list2 = extract_text_from_pdf(file_path2)
    print(f"{text_list2}")
    print(f"Total number of words: {len(text_list2)}")

    is_in_list(text_list, text_list2)


if __name__ == '__main__':
    main()
