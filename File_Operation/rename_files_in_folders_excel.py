import os

import pandas as pd
from fuzzywuzzy import fuzz


def rename_files_based_on_excel(excel_file_path, folder_path, error_file_path, extension="pdf", similarity_percentage=-1):
    """
    Renames files in a folder based on a mapping provided in an Excel file. The input Excel file doesn’t need a fixed header. The code uses the first
    and second columns as the old and new file names, respectively, as specified by the skiprows=0 parameter

    Parameters:
    excel_file_path (str): Path to the Excel file containing old and new file names.
    folder_path (str): Path to the folder where the files are located.
    error_file_path (str): Path to the file where errors will be logged.
    extension (str): File extension of the files to be renamed (default is "pdf").
    similarity_percentage (int): Minimum similarity percentage for renaming (default is 100).
    """
    # Read the Excel file into a DataFrame, skipping the first row (header)
    df = pd.read_excel(excel_file_path, skiprows=0)  # skiprows=0 indicates that the reading starts from the first row (index 0), no headers

    # Open the error file in append mode with UTF-8 encoding to handle special characters
    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        # Iterate over each row in the DataFrame
        n = 0
        for index, row in df.iterrows():
            n += 1
            print(f"Row {n}")

            # Extract the old and new file names from the current row
            old_file_name = row.iloc[0]
            new_file_name = row.iloc[1]

            # Construct the full path for the old and new files
            old_file_path = os.path.join(folder_path, f"{old_file_name}.{extension}")
            new_file_path = os.path.join(folder_path, f"{new_file_name}.{extension}")

            # Check if the old file exists
            if os.path.exists(old_file_path):
                # Calculate the similarity ratio between old and new file names
                similarity = fuzz.ratio(old_file_name, new_file_name)

                # Rename the file if the similarity meets or exceeds the specified percentage
                if similarity_percentage == -1 or similarity >= similarity_percentage:
                    os.rename(old_file_path, new_file_path)
                    print(f"Old: {old_file_name} \nNew: {new_file_name}")

            else:
                # Log an error if the old file does not exist
                error_file.write(f"File not found: {old_file_path}\n")


def main():
    """
    Main function to set parameters and call the renaming function.
    """
    excel_file_path = r"D:\YK\Downloads\Book\_Summary.xlsx"  # Path to the Excel file with file name mappings
    folder_path = r"D:\YK\Downloads\Book"  # Folder containing the files to be renamed
    extension = "epub"  # File extension of the files to be renamed
    similarity_percentage = -1  # Minimum similarity percentage for renaming
    error_file_path = r"D:\YK\Downloads\error.txt"  # Path to the error log file

    # Call the function to rename files based on the Excel mapping
    rename_files_based_on_excel(excel_file_path, folder_path, error_file_path, extension, similarity_percentage)


# Entry point of the script
if __name__ == "__main__":
    main()
