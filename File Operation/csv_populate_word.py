from tkinter import filedialog

import pandas as pd
from docxtpl import DocxTemplate

from config import filename, list_of_placeholders


def csv_populate_word(filename, list_of_placeholders):
    """iterate through each row in the CSV file, replacing placeholders in the Word file with the values from each
    row."""
    folder = filedialog.askdirectory()
    docx = DocxTemplate(filedialog.askopenfilename(filetypes=[("Word Files", ".docx .doc")]))
    csv = filedialog.askopenfilename(filetypes=[("Excel Files", ".xlsx .xls .csv")])

    # values that populate word file: dictionary = {placeholder : value}
    my_context = {filename: filename}
    # add the values to the dictionary
    for value in list_of_placeholders:
        my_context[value] = value

    # read csv
    dataframe = pd.read_csv(csv)

    for index, row in dataframe.iterrows():
        context = {filename: row[filename]}
        # add the values to the dictionary
        for value in list_of_placeholders:
            context[value] = row[value]

        file = row[filename]

        # open, update & save the doc from the template
        my_context.update(context)
        docx.render(my_context)
        docx.save(f"{folder}/{file}.docx")


def main():
    csv_populate_word(filename, list_of_placeholders)
    print("done")


if __name__ == '__main__':
    main()
