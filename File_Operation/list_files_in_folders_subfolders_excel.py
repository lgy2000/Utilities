import os

import pandas as pd


def list_files_to_excel(folder_path, excel_file_path):
    data = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file_name in filenames:
            full_file_path = os.path.join(dirpath, file_name)
            folder_name = os.path.basename(dirpath)
            file_name_without_ext, extension = os.path.splitext(file_name)
            data.append([folder_name, file_name_without_ext, extension, full_file_path])

    df = pd.DataFrame(data, columns=["Folder Name", "File Name", "Extension", "Full File Path"])
    df = df[["Folder Name", "File Name", "Extension", "Full File Path"]]  # Reordering the columns
    df.to_excel(excel_file_path, index=False)


if __name__ == "__main__":
    folder_path = (r"E:\All\6 Resources\6.1 Non-Technical Books\6.1.9 Book Summaries")  # replace with your folder path
    excel_file_path = folder_path + r"\_Summary.xlsx"  # replace with your Excel file path
    list_files_to_excel(folder_path, excel_file_path)
