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
    folder_path = (r"D:\YK\Honeywell\2024 MYP-000360 Biocon BMS & EMS HMI Replacement\1 Project Document\3.0 Project Engineering\Manual\Vendor "
    r"Documents")  # replace with your folder path
    excel_file_path = folder_path + r"\_Summary2.xlsx"  # replace with your Excel file path
    list_files_to_excel(folder_path, excel_file_path)
