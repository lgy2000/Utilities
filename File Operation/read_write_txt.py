"""
read_write_txt.py

Description:
Write text to .txt file

Notes:
- Only applicable to .txt file
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
