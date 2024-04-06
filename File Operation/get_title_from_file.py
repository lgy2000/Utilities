"""
Module name: get_title_from_file.py

Description:
Extracts the title from a PDF file based on a specified keyword present in the file's content.

Notes:
- The module utilizes the `PyPDF2` library for PDF processing and the `tkinter` library for GUI functionality.
- The `get_title_from_text()` function extracts the title from a page text based on a given keyword. It splits the text using the keyword and
retrieves the second part, which is assumed to be the title.
- The `get_title_from_file()` function iterates through each page of the PDF file, extracts text, and searches for the specified keyword. Once
found, it calls `get_title_from_text()` to extract the title from that page.
- The `main()` function prompts the user to select a PDF file via a GUI dialog if `show_file_dialog` is set to True in the `config.py` file,
otherwise it uses the `input_file` specified in `config.py`.
- It then extracts the title from the selected PDF file based on the specified keyword and prints the title if found, otherwise prints "Title not
found."
"""

from tkinter import filedialog

import PyPDF2

from config import show_file_dialog, input_file, keyword


def get_title_from_text(keyword, page_text):
    # Split the text using the title identifier
    title_parts = page_text.split(keyword) if keyword in page_text else page_text.split(keyword.upper())
    # Get the second part (the title itself)
    title = title_parts[-1].strip().replace(":", "").replace("  ", " ").replace("  ", " ")
    # If there are multiple lines in the title, combine them into one string
    title = " ".join(title.splitlines()[:3])[:60]
    return title


def get_title_from_file(file, keyword):
    # Open the PDF file in binary mode
    with open(file, 'rb') as f:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(f)

        # Initialize an empty title
        title = None

        # Iterate through each page in the PDF
        for page_num in range(len(reader.pages)):
            # Extract text from the current page
            page_text = reader.pages[page_num].extract_text()
            print(page_text)

            # Search for the title block in the extracted text
            # You can customize this based on the actual structure of your PDF
            if keyword in page_text or keyword.upper() in page_text:
                return get_title_from_text(keyword, page_text)
        return title


def main():
    if show_file_dialog == 1:
        file = filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf")])
    else:
        file = input_file
    title = get_title_from_file(file, keyword)
    if title:
        print("Title:", title)
    else:
        print("Title not found.")


if __name__ == '__main__':
    main()
