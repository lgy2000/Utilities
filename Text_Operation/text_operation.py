# !/usr/bin/env python3

"""
text_operation.py

Provides operations for modifying and handling text.

Description:
This module provides a variety of operations for handling and modifying text. It includes functionality to add or remove prefixes and suffixes,
change the case of text, and extract titles from text. The module uses the `os` and `datetime` modules for file system operations and date-time
manipulation respectively. It also imports functionality from the `get_title_from_pdf.py` module for extracting titles from PDF files.
"""

import os
from datetime import datetime
from enum import Enum


class Prefix(Enum):
    NONE = 0
    ADD_COUNTER = 1
    ADD_TIMESTAMP = 2
    ADD_CUSTOM = 3


class Suffix(Enum):
    NONE = 0
    ADD_COUNTER = 1
    ADD_TIMESTAMP = 2
    ADD_CUSTOM = 3


class Case(Enum):
    NONE = 0
    TITLE = 1
    UPPER = 2
    LOWER = 3


class TextOperation:
    def __init__(self, text: str,
                 add_title: bool = False,
                 prefix_operation: Prefix = Prefix.NONE,
                 suffix_operation: Suffix = Suffix.NONE,
                 case_operation: Case = Case.NONE,
                 prefix: str = "",
                 suffix: str = "",
                 page_text: str = "",
                 title_keyword: str = "Title",
                 remove_prefix: bool = False,
                 prefix_delimiter: str = ""):
        self.text = text
        self.add_title = add_title
        self.prefix_operation = prefix_operation
        self.suffix_operation = suffix_operation
        self.case_operation = case_operation
        self.prefix = prefix
        self.suffix = suffix
        self.page_text = page_text
        self.title_keyword = title_keyword if self.add_title else ""
        self.remove_prefix = remove_prefix
        self.prefix_delimiter = prefix_delimiter

    def set_args(self, args):
        self.add_title = args.add_title
        self.title_keyword = args.title_keyword if self.add_title == 1 else ""
        self.prefix_operation = args.prefix_operation
        self.suffix_operation = args.suffix_operation
        self.case_operation = args.case_operation.upper()
        self.prefix = args.prefix if self.prefix_operation == Prefix.ADD_CUSTOM else ""
        self.suffix = args.suffix if self.suffix_operation == Suffix.ADD_CUSTOM else ""
        self.remove_prefix = args.remove_prefix
        self.prefix_delimiter = args.prefix_delimiter if self.remove_prefix == 1 else ""

    def set_counter(self, counter):
        self.prefix = self.get_prefix(counter)
        self.suffix = self.get_suffix(counter)

    def process_text(self):
        text = self.text
        if self.remove_prefix:
            text = self._remove_prefix()
        text = f"{self.prefix}{text}{self.suffix}"
        self.text = text
        self.text = self.change_case()
        return self.text

    def clean_string(self):
        self.text = self.text.strip()  # Remove leading and trailing whitespace
        self.text = ' '.join(self.text.split())  # Remove extra spaces
        self.text = self.text.translate(str.maketrans('', '', '?!@$%^*:/\\=+{}<>'))  # Remove specific symbols
        return self.text

    def get_title_from_text(self, page_text, title_keyword):
        self.title_keyword = title_keyword
        # Split the text using the title identifier
        # print(page_text)
        if self.title_keyword in page_text:
            title_parts = page_text.split(self.title_keyword)
        elif self.title_keyword.upper() in page_text:
            title_parts = page_text.split(self.title_keyword.upper())
        else:
            title_parts = page_text.split(self.title_keyword.capitalize())
        # print(title_parts)

        # Get the second part in a list (the title itself)
        try:
            title = title_parts[1]
            # print(title)

            # Clean the title
            self.text = title
            self.text = self.clean_string()
            # If there are multiple lines in the title, combine them into one string
            self.text = " ".join(self.text.splitlines()[:3])[:60]
            # print(self.text)
        except IndexError:
            if title_parts:
                self.text = title_parts
                print("Title not found.")
            else:
                print("Text not found in the file.")
        return self.text

    def _remove_prefix(self) -> str:
        if self.remove_prefix == 1:
            parts = self.text.split(self.prefix_delimiter, 1)  # Split only once
            if len(parts) > 1:
                self.text = parts[1]
        return self.text

    def get_prefix(self, counter: int) -> str:
        """Get prefix based on the prefix operation."""
        if self.prefix_operation == Prefix.ADD_COUNTER:
            self.prefix = f"{counter} "
            return self.prefix
        elif self.prefix_operation == Prefix.ADD_TIMESTAMP:
            self.prefix = f"{datetime.fromtimestamp(os.stat(self.text).st_mtime)} "
            return self.prefix
        elif self.prefix_operation == Prefix.ADD_CUSTOM:
            self.prefix = f"{self.prefix} "
            return self.prefix
        else:
            return self.text

    def get_suffix(self, counter: int) -> str:
        """Get prefix based on the suffix operation."""
        if self.suffix_operation == Suffix.ADD_COUNTER:
            self.suffix = f" {counter}"
            return self.suffix
        elif self.suffix_operation == Suffix.ADD_TIMESTAMP:
            self.suffix = f" {datetime.fromtimestamp(os.stat(self.text).st_mtime)}"
            return self.suffix
        elif self.suffix_operation == Suffix.ADD_CUSTOM:
            self.suffix = f" {self.suffix}"
            return self.suffix
        else:
            return self.suffix

    def change_case(self) -> str:
        """Change the case of the text based on the case operation."""
        if self.case_operation == Case.TITLE:
            self.text = self.get_title_case()
            return self.text
        elif self.case_operation == Case.UPPER:
            self.text = self.text.upper()
            return self.text
        elif self.case_operation == Case.LOWER:
            self.text = self.text.lower()
            return self.text
        else:
            return self.text

    def get_title_case(self):
        """return the text in title case"""
        # List of small words to exclude from capitalization
        small_words = ['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'if', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet']

        # Convert the text to title case
        title_case_text = self.text.title()
        # Split the title case text into words
        words = title_case_text.split()
        # Convert the small words back to lowercase, unless it's the first word
        title_words = [word.lower() if word.lower() in small_words and index != 0 else word for index, word in enumerate(words)]

        # Join the title case words back into a string
        self.text = ' '.join(title_words)
        return self.text
