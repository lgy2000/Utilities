"""
Module name: read_write_txt.py

Description:
Reads the contents of a text file and overwrites it with a specified text input.

Notes:
- The module utilizes the `tkinter` library for GUI functionality to prompt the user to select a text file.
- The `read_write_txt()` function prompts the user to select a text file via a GUI dialog and overwrites its contents with the specified text input.
- The input text is provided by the `text_input` argument of the function.
- The function first opens the selected file in read-write mode, writes the input text to it, and then closes the file.
- It then reopens the file in read mode to ensure that the latest changes are read.
- The `main()` function is provided for standalone execution, which initiates the text read-write process and prints "done" upon completion.
"""

from tkinter import filedialog, Tk

# Input
text = "SANTA"


def read_write_txt(text_input):
    # function that read & write .docx file
    root = Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()

    # Read & write file
    file = open(filename, 'r+', encoding='utf-8')
    file.write(str(text_input))
    file.close()

    # Read the latest file
    file = open(filename, 'r', encoding='utf-8')
    file.close()


def main():
    read_write_txt(text)
    print('done')


if __name__ == '__main__':
    main()