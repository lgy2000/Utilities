import os
from datetime import datetime


class TextOperation:
    def __init__(self, text,
                 to_get_title_from_file=0,
                 to_remove_prefix=0,
                 to_add_prefix=0,
                 to_add_suffix=0,
                 to_change_case=0,
                 prefix="",
                 suffix="",
                 page_text="",
                 keyword="Title",
                 prefix_delimiter=" ",
                 prefix_str="",
                 suffix_str=""):
        self.text = text
        self.to_get_title_from_file = to_get_title_from_file
        self.to_remove_prefix = to_remove_prefix
        self.to_add_prefix = to_add_prefix
        self.to_add_suffix = to_add_suffix
        self.to_change_case = to_change_case

        self.prefix = prefix
        self.suffix = suffix
        self.page_text = page_text
        self.keyword = keyword if self.to_get_title_from_file == 1 else ""
        self.prefix_delimiter = prefix_delimiter if self.to_remove_prefix == 1 else ""
        self.prefix_str = prefix_str if self.to_add_prefix == 3 else ""
        self.suffix_str = suffix_str if self.to_add_suffix == 3 else ""

    def clean_string(self):
        self.text = self.text.strip()  # Remove leading and trailing whitespace
        self.text = ' '.join(self.text.split())  # Remove extra spaces
        self.text = self.text.translate(str.maketrans('', '', '?!@$%^*:/\\=+{}<>'))  # Remove specific symbols
        return self.text

    def get_title_from_text(self, page_text, keyword):
        self.keyword = keyword
        # Split the text using the title identifier
        # print(page_text)
        if self.keyword in page_text:
            title_parts = page_text.split(self.keyword)
        elif self.keyword.upper() in page_text:
            title_parts = page_text.split(self.keyword.upper())
        else:
            title_parts = page_text.split(self.keyword.capitalize())
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

    def remove_prefix(self):
        if self.to_remove_prefix == 1:
            parts = self.text.split(self.prefix_delimiter)
            if len(parts) > 1:
                self.text = self.prefix_delimiter.join(parts[1:])
                return self.text
        return self.text

    def get_prefix(self, counter):
        """return the prefix"""
        if self.to_add_prefix == 0:
            self.prefix = ""
            return self.prefix
        elif self.to_add_prefix == 1:
            self.prefix = f"{counter} "
            return self.prefix
        elif self.to_add_prefix == 2:
            self.prefix = f"{datetime.fromtimestamp(os.stat(self.prefix).st_mtime)} "
            return self.prefix
        elif self.to_add_prefix == 3:
            self.prefix = f"{self.prefix_str} "
            return self.prefix

    def get_suffix(self, counter):
        """return the suffix"""
        if self.to_add_suffix == 0:
            self.suffix = ""
            return self.suffix
        elif self.to_add_suffix == 1:
            self.suffix = f" {counter}"
            return self.suffix
        elif self.to_add_suffix == 2:
            self.suffix = f" {datetime.fromtimestamp(os.stat(self.text).st_mtime)}"
            return self.suffix
        elif self.to_add_suffix == 3:
            self.suffix = f" {self.suffix_str}"
            return self.suffix

    def change_case(self):
        """return the text in selected case"""
        if self.to_change_case == 1:
            self.text = self.get_title_case()
            return self.text
        elif self.to_change_case == 2:
            self.text = self.text.upper()
            return self.text
        elif self.to_change_case == 3:
            self.text = self.text.lower()
            return self.text
        return self.text

    def get_title_case(self):
        """return the text in title case"""
        # List of small words to exclude from capitalization
        small_words = ['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'if', 'in', 'nor', 'of', 'on', 'or', 'so', 'the',
                       'to', 'up', 'yet']

        # Split the text into words
        words = self.text.split()

        # Convert the first letter of each word to uppercase, unless it's a small word and not the first word
        title_words = [word.capitalize() if word.lower() not in small_words or index == 0 else word for index, word in
                       enumerate(words)]
        # Join the title case words back into a string
        self.text = ' '.join(title_words)
        return self.text
