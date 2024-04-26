# !/usr/bin/env python3

"""
modify_text.py

Modifies text based on specified configurations.

Description:
This module provides functionality to modify text according to user-specified configurations. It includes options to add or remove prefixes and
suffixes, change case, and extract titles from files. The module uses the `os` and `datetime` modules for file system operations and date-time
manipulation respectively. It also imports functionality from the `extract_title_from_pdf.py` module for extracting titles from PDF files.
"""

from PDF_Operation.pdf_operation import PdfOperation
from config import input_text
from text_operation import TextOperation


def main():
    pdf_ops = PdfOperation()
    text_ops = TextOperation(text=input_text, add_title=0,
                             remove_prefix=0,
                             to_add_prefix=0,
                             to_add_suffix=0,
                             to_change_case=0,
                             prefix="",
                             suffix="",
                             page_text="",
                             title_keyword="Title",
                             prefix_delimiter=" ",
                             prefix_str="",
                             suffix_str="")
    counter = ""
    text_ops.text = text_ops.remove_prefix()
    prefix = text_ops.get_prefix(counter)
    suffix = text_ops.get_suffix(counter)
    title = pdf_ops.extract_title_from_pdf(file="", title_keyword="Title")
    text_ops.text = f"{prefix}{text_ops.text}{suffix}{title}"
    text_ops.text = text_ops.change_case()

    print(text_ops.text)
    return text_ops.text


if __name__ == '__main__':
    main()
