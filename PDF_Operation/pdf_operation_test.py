"""
pdf_operation_test.py

Contains unit tests for the pdf_operation module.

Description:
This module contains unit tests for the pdf_operation module.
It includes tests for deleting pages, rotating pages, and checking if a string is present in a PDF file.
It uses the unittest module for unit testing and the PyPDF2 library for PDF file operations.
"""

import os
import shutil
import unittest

from PyPDF2 import PdfReader

from pdf_operation import PdfOperation


class TestPdfOperation(unittest.TestCase):
    def setUp(self):
        self.pdf_ops = PdfOperation()
        base_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
        self.folder = ".test"
        self.test_file = os.path.join(base_dir, self.folder, "test1.pdf")
        self.test_file_copy = os.path.join(base_dir, self.folder, "test1-2.pdf")
        self.test_folder = os.path.join(base_dir, self.folder, "test1")
        self.test_folder_copy = os.path.join(base_dir, self.folder, "test1-2")

        self.test_string_page_0 = "Aenean pulvinar euismod ligula at lacinia. Ut consectetur dui ipsum, a rhoncus lacus gravida"  # replace with a
        # string
        self.test_string_page_1 = "rgar234 gsrg234 srgar"  # replace with a string
        self.rotation_angle = 90

    def test_delete_pdf_page_1(self):
        # Test that the delete_pdf_page method works correctly
        initial_num_pages = len(PdfReader(self.test_file).pages)
        initial_string_presence = self.pdf_ops.is_string_in_pdf(self.test_file, self.test_string_page_0)

        shutil.copy(self.test_file, self.test_file_copy)
        self.pdf_ops.delete_pdf_page(self.test_file_copy, 0)
        final_num_pages = len(PdfReader(self.test_file_copy).pages)
        final_string_presence = self.pdf_ops.is_string_in_pdf(self.test_file_copy, self.test_string_page_0)

        self.assertEqual(final_num_pages, initial_num_pages - 1)
        self.assertTrue(initial_string_presence)
        self.assertFalse(final_string_presence)
        os.remove(self.test_file_copy)

    def test_rotate_pdf(self):
        initial_rotations = self.pdf_ops.check_pdf_rotation(self.test_file)

        shutil.copy(self.test_file, self.test_file_copy)
        self.pdf_ops.rotate_pdf(self.test_file_copy, self.rotation_angle)

        # Check the final rotation of each page in the PDF file
        final_rotations = self.pdf_ops.check_pdf_rotation(self.test_file_copy)

        # Check if the rotation was successful
        for i in range(len(initial_rotations)):
            expected_rotation = (initial_rotations[i] + self.rotation_angle) % 360
            self.assertEqual(final_rotations[i], expected_rotation, f"Page {i + 1} rotation failed")

        # Clean up the test file copy
        os.remove(self.test_file_copy)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
