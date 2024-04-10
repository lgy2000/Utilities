"""
Module name: modify_text.py

Description:
Modifies text based on specified configurations, such as adding prefixes or suffixes, removing prefixes, adding titles, and changing text case.

Notes:
- The module utilizes the `os` and `datetime` modules for file system operations and date-time manipulation respectively.
- It also imports functionality from the `get_title_from_pdf.py` module for extracting titles from PDF files.
- The `remove_prefix()` function removes prefixes from the input text based on the specified configuration.
- The `get_prefix()` function adds prefixes to the input text based on the specified configuration, including options for counters, timestamps,
and custom strings.
- The `get_suffix()` function adds suffixes to the input text based on the specified configuration, similar to the `get_prefix()` function.
- The `get_title_from_pdf()` function retrieves titles from PDF files if enabled in the configuration.
- The `change_case()` function modifies the case of the input text based on the specified configuration, including options for title case,
uppercase, and lowercase.
- The `main()` function orchestrates the text modification process according to the specified configurations and prints the modified text.
"""

from PDF_Operation.pdf_operation import PdfOperation
from config import input_text
from text_operation import TextOperation


def main():
    pdf_ops = PdfOperation()
    text_ops = TextOperation(text=input_text, to_get_title_from_file=0,
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
                             suffix_str="")
    counter = ""
    text_ops.text = text_ops.remove_prefix()
    prefix = text_ops.get_prefix(counter)
    suffix = text_ops.get_suffix(counter)
    title = pdf_ops.get_title_from_pdf(file="", keyword="Title")
    text_ops.text = f"{prefix}{text_ops.text}{suffix}{title}"
    text_ops.text = text_ops.change_case()

    print(text_ops.text)
    return text_ops.text


if __name__ == '__main__':
    main()
