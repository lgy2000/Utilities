"""
pdf_operation.py

Provides a set of operations for manipulating PDF files.

Description:
This module provides a set of operations for manipulating PDF files. It includes functions for deleting pages, rotating pages, extracting text from
a PDF file, checking if a string is present in a PDF file, and extracting a title from a PDF file. It uses the PyPDF2 and pikepdf libraries for PDF
file operations.
"""

import logging
import os

import pikepdf
from PyPDF2 import PdfReader, PdfWriter

from File_Operation.text_operation import TextOperation


class PdfOperation:
    def __init__(self):
        self.text_ops = TextOperation(text="")

    @staticmethod
    def delete_pdf_page(filepath: str, page_number: int) -> None:
        """Delete a specific page from a PDF file."""
        try:
            with pikepdf.Pdf.open(filepath, allow_overwriting_input=True) as pdf:
                del pdf.pages[page_number]
                pdf.save(filepath)
                logging.info(f"Modified file {filepath}")
        except IndexError:
            logging.error(f"Page number {page_number} out of range in file:\n{filepath}")
        except Exception as e:
            logging.error(f"Error processing file {filepath}:\n{e}")

    def delete_pdf_page_in_folder(self, folder: str, page_number: int) -> None:
        """Delete a specific page from all PDF files within a folder."""
        for filename in os.listdir(folder):
            if filename.endswith('.pdf'):
                filepath = os.path.join(folder, filename)
                self.delete_pdf_page(filepath, page_number)

    @staticmethod
    def rotate_pdf_page(angle: int, reader: PdfReader, writer: PdfWriter) -> None:
        """Rotate each page in a PDF file by a specified angle."""
        try:
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                page.rotate(angle)
                writer.add_page(page)
            logging.info(f"Rotated all pages by {angle} degrees.")
        except Exception as e:
            logging.error(f"Error rotating pages: {e}")

    def rotate_pdf(self, file: str, angle: int) -> None:
        """Rotate each page in a PDF file by a specified angle."""
        with open(file, 'rb') as f:
            reader = PdfReader(f)
            writer = PdfWriter()
            self.rotate_pdf_page(angle, reader, writer)
            with open(file, 'wb') as output_pdf:
                writer.write(output_pdf)

    def rotate_pdf_in_folder(self, folder: str, angle: int) -> None:
        """Rotate each page in all PDF files within a folder by a specified angle."""
        for filename in os.listdir(folder):
            if filename.endswith('.pdf'):
                file = os.path.join(folder, filename)
                self.rotate_pdf(file, angle)

    @staticmethod
    def check_pdf_rotation(file_path):
        pdf = PdfReader(file_path)
        rotations = []
        for page in range(len(pdf.pages)):
            rotation = pdf.pages[page].get('/Rotate', 0)
            rotations.append(rotation)
        return rotations

    def is_string_in_pdf(self, file_path, search_string):
        content = self.get_text_from_pdf(file_path)
        return search_string in content

    @staticmethod
    def get_text_from_pdf(file_path):
        pdf = PdfReader(file_path)
        text = ""
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()
        return text

    def get_title_from_pdf(self, file, keyword):
        # Extract text from the PDF file
        page_text = self.get_text_from_pdf(file)
        # Search for the title block in the extracted text
        if self.text_ops.keyword in page_text or self.text_ops.keyword.upper() in page_text or self.text_ops.keyword.capitalize() in page_text:
            return self.text_ops.get_title_from_text(page_text, keyword)
        return None
