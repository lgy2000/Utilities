# !/usr/bin/env python3

"""
pdf_operation.py

Provides a set of operations for manipulating PDF files.

Description:
This module includes functions for deleting pages, rotating pages, extracting text from a PDF file, checking if a string is present in a PDF file,
extracting a title from a PDF file and compressing PDF file. It uses the PyPDF2 and pikepdf libraries for PDF file operations.
"""

import glob
import logging
import os
import re
import shutil
import time
import zipfile
from datetime import date
from fnmatch import fnmatch
from pathlib import Path

import pikepdf
from PyPDF2 import PdfReader, PdfWriter
from pylovepdf.ilovepdf import ILovePdf
from pypdf import PdfWriter

from Text_Operation.text_operation import TextOperation


class PdfOperation:
    def __init__(self):
        self.text_ops = TextOperation(text="")

    @staticmethod
    def get_current_folder_path():
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return current_dir

    def get_parent_folder_path(self):
        current_dir = self.get_current_folder_path()
        # Go up one level
        parent_dir = os.path.dirname(current_dir)
        return parent_dir

    @staticmethod
    def delete_pdf_page(file: str, page_number: int) -> None:
        """Delete a specific page from a PDF file."""
        try:
            if file.endswith('.pdf'):
                with pikepdf.Pdf.open(file, allow_overwriting_input=True) as pdf:
                    del pdf.pages[page_number]
                    pdf.save(file)
                    logging.info(f"Modified file {file}")
        except IndexError:
            logging.error(f"Page number {page_number} out of range in file:\n{file}")
        except Exception as e:
            logging.error(f"Error processing file {file}:\n{e}")

    def delete_pdf_page_in_folder(self, folder: str, page_number: int) -> None:
        """Delete a specific page from all PDF files within a folder and its subfolders."""
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    self.delete_pdf_page(file_path, page_number)

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
        if file.endswith('.pdf'):
            with open(file, 'rb') as f:
                reader = PdfReader(f)
                writer = PdfWriter()
                self.rotate_pdf_page(angle, reader, writer)
                with open(file, 'wb') as output_pdf:
                    writer.write(output_pdf)

    def rotate_pdf_in_folder(self, folder: str, angle: int) -> None:
        """Rotate each page in all PDF files within a folder and its subfolders by a specified angle."""
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    self.rotate_pdf(file_path, angle)

    @staticmethod
    def check_pdf_rotation(file_path):
        """Returns a list of rotation angles for each page in a PDF file."""
        pdf = PdfReader(file_path)
        rotations = []
        for page in range(len(pdf.pages)):
            rotation = pdf.pages[page].get('/Rotate', 0)
            rotations.append(rotation)
        return rotations

    def is_string_in_pdf(self, file_path, search_string):
        """Checks if a given string is present in the text of a PDF file."""
        content = self.get_text_from_pdf(file_path)
        return search_string in content

    @staticmethod
    def get_text_from_pdf(file_path):
        """Extracts and returns all text from a PDF file."""
        pdf = PdfReader(file_path)
        text = ""
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()
        return text

    def extract_title_from_pdf(self, file, title_keyword):
        """Extracts and returns the title from a PDF file based on a keyword."""
        # Extract text from the PDF file
        page_text = self.get_text_from_pdf(file)
        # Search for the title block in the extracted text
        if title_keyword in page_text or title_keyword.upper() in page_text or title_keyword.capitalize() in page_text:
            return self.text_ops.get_title_from_text(page_text, title_keyword)
        return None

    def compress_pdf_folder_ilovepdf(self, action_path, compress_level, all_pdfs_pattern, compressed_pdfs_pattern, compressed_zip_pattern,
                                     compressed_file_regex_pattern, compressed_file_regex_pattern2, output_errors, public_key1, public_key2,
                                     public_key3):
        pdf_files = []
        zip_file_location = ""
        compressed_pdfs = []
        subdirectories = []

        # Define the parent path
        parent_path = os.path.dirname(action_path)
        parent_folder_name = os.path.basename(parent_path)
        action_folder_name = os.path.basename(action_path)
        print(f"\n\n\nAction Path: {action_path}")
        print(f"Parent path: {parent_path}\n")

        # Walk through the directory to find all PDF files
        for path, subdirs, files in os.walk(action_path):
            for file in files:
                if fnmatch(file, all_pdfs_pattern):
                    pdf_files.append(os.path.join(path, file))
            for subdir in subdirs:
                subdirectories.append(subdir)

        if action_path.endswith('.pdf'):
            pdf_files.append(action_path)

        # Initialize the ILovePdf object and create a new task
        ilovepdf = ILovePdf(public_key1, verify_ssl=True)
        task = ilovepdf.new_task(compress_level)

        if pdf_files:
            date_today = date.today().strftime("%Y-%m-%d, %A")
            logging.info(f"\n\nCompressed PDFs on {date_today}\n")
            logging.info(f"Action Path: {action_path}")
            logging.info(f"Parent path: {parent_path}\n")

            # Upload all the PDF files to the task
            for file in pdf_files:
                print("Upload: " + str(file))
                task.add_file(file)
                task.set_output_folder(parent_path)
                task.file.set_metas('Title', file)

            # Execute the task, download the result, and delete the task
            try:
                task.execute()
                task.download()
                task.delete_current_task()

                # Wait for the task to finish
                time.sleep(3)

                # Unzip the downloaded compressed PDF files
                logging.debug(f"\nSearch Zip file: {parent_path}\\{compressed_zip_pattern}")
                zip_file_location = glob.glob(parent_path + "\\" + compressed_zip_pattern)[0]
                logging.debug(f"Zip file location: {zip_file_location}")
                with zipfile.ZipFile(zip_file_location, 'r') as zip_ref:
                    zip_ref.extractall(parent_path)
                print(f"Zip file extracted: {zip_file_location}\n")

                # Check if the zip extraction path is correct, if not move to correct path
                wrong_zip_path = str(os.path.join(parent_path, parent_folder_name, action_folder_name))
                correct_zip_path = str(os.path.join(parent_path, action_folder_name))
                if os.path.exists(wrong_zip_path):
                    print("Move zip files with wrong path to the correct path")
                    # Merge the directories
                    for src_dir, dirs, files in os.walk(wrong_zip_path):
                        dst_dir = src_dir.replace(wrong_zip_path, correct_zip_path, 1)
                        for file_ in files:
                            src_file = os.path.join(src_dir, file_)
                            dst_file = os.path.join(dst_dir, file_)
                            print("Compressed file: " + src_file)
                            print("Compressed file: " + dst_file)
                            if os.path.exists(dst_file):
                                print(f"File already exists: {dst_file}")
                            shutil.move(src_file, dst_dir)

                # Wait for the extraction to finish
                time.sleep(3)

                # Find all the compressed PDFs recursively
                compressed_pdfs = glob.glob(os.path.join(action_path, '**', compressed_pdfs_pattern), recursive=True)
                logging.debug(f"Compressed PDFs: {compressed_pdfs}\n")
                print("\n")

            except Exception as e:
                output_errors += f"\n{e}\n"

            # Replace the original PDF files with the compressed ones
            for compressed_file_path in compressed_pdfs:
                compressed_file_name = os.path.split(compressed_file_path)[1]

                # Remove the compressed file regex pattern from the compressed file name
                if re.search(compressed_file_regex_pattern, compressed_file_name):
                    compressed_file_name = re.sub(compressed_file_regex_pattern, '', compressed_file_name)
                else:
                    compressed_file_name = compressed_file_name.replace(compressed_file_regex_pattern2, '')

                file_name = os.path.splitext(compressed_file_name)[0]
                for original_file_path in pdf_files:
                    original_file_name = os.path.split(original_file_path)[1]
                    original_file_name = os.path.splitext(original_file_name)[0]

                    # Determine original file which does not contain "compress" string
                    if "compress" not in original_file_name:

                        # Remove the folder name from the compressed file name if exists
                        folder_name = os.path.split(os.path.split(original_file_path)[0])[1]

                        compressed_original_file_name = file_name + ".pdf"

                        # Check if the original file name matches the compressed file name
                        if compressed_original_file_name == original_file_path:
                            # the folder name (potentially followed by one or two characters ??), is replaced with an empty string
                            compressed_file_name = re.sub(f"{folder_name}??", '', compressed_file_name)

                        # Check if the original file name matches the compressed file name
                        if file_name in original_file_path:
                            # Check if compressed and original file exists
                            if os.path.exists(Path(original_file_path).resolve()) and os.path.exists(Path(compressed_file_path).resolve()):
                                logging_replace = f"Replace: \t{compressed_file_path}\nto: \t\t{original_file_path}"
                                print(logging_replace)
                                shutil.move(Path(compressed_file_path), Path(original_file_path))
                            else:
                                output_errors += f"\n\033[91mFile Replacing Error\033[0m\n{logging_replace}\n"

            # Delete the zip file
            if zip_file_location:
                os.remove(zip_file_location)

        # If there are any errors, print them at once
        if len(output_errors) > 0:
            print("\n\033[91mFILES THAT COULDN'T BE REPLACED BY THE SCRIPT HAVE TO BE MANUALLY REPLACED\033[0m")
            print(output_errors)

    def compress_pdf_file_ilovepdf(self, action_path, compress_level, compressed_pdfs_pattern, output_errors, public_key1, public_key2, public_key3):
        compressed_pdfs = []

        # Define the parent path
        parent_path = os.path.dirname(action_path)
        print(f"\n\n\nAction Path: {action_path}")
        print(f"Parent path: {parent_path}\n")

        # Initialize the ILovePdf object and create a new task
        ilovepdf = ILovePdf(public_key1, verify_ssl=True)
        task = ilovepdf.new_task(compress_level)

        date_today = date.today().strftime("%Y-%m-%d, %A")
        logging.info(f"\n\nCompressed PDFs on {date_today}\n")
        logging.info(f"Action Path: {action_path}")
        logging.info(f"Parent path: {parent_path}\n")

        # Execute the task, download the result, and delete the task
        try:
            print("Upload: " + str(action_path))
            task.add_file(action_path)
            task.set_output_folder(parent_path)
            task.file.set_metas('Title', action_path)
            task.execute()
            task.download()
            task.delete_current_task()

            # Wait for the task to finish
            time.sleep(3)

            # Find all the compressed PDFs recursively
            compressed_pdfs = glob.glob(os.path.join(parent_path, '**', compressed_pdfs_pattern), recursive=True)
            logging.debug(f"Compressed PDFs: {compressed_pdfs}\n")
            print("\n")

        except Exception as e:
            output_errors += f"\n{e}\n"

        # Replace the original PDF files with the compressed ones
        for compressed_file_path in compressed_pdfs:
            # Check if compressed and original file exists
            if os.path.exists(Path(action_path).resolve()) and os.path.exists(Path(compressed_file_path).resolve()):
                logging_replace = f"Replace: \t{compressed_file_path}\nto: \t\t{action_path}"
                print(logging_replace)
                shutil.move(Path(compressed_file_path), Path(action_path))
            else:
                output_errors += f"\n\033[91mFile Replacing Error\033[0m\n{logging_replace}\n"

            # If there are any errors, print them at once
        if len(output_errors) > 0:
            print("\n\033[91mFILES THAT COULDN'T BE REPLACED BY THE SCRIPT HAVE TO BE MANUALLY REPLACED\033[0m")
            print(output_errors)
