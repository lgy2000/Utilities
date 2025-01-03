import csv
import os

import openpyxl

# Define the working file path
excel_file_path = (r"D:\YK\Honeywell\2024 MYP-000360 Biocon BMS EMS\1 Project Document\3.0 Project Engineering\Network Switch Port Assignment\IP "
                   r"Address.xlsx")
current_directory = os.path.dirname(os.path.abspath(excel_file_path))
csv_file_name = 'sheet_names.csv'
csv_file_path = os.path.join(current_directory, csv_file_name)

# Load the existing Excel file
wb = openpyxl.load_workbook(excel_file_path)

# Get all sheet names
sheet_names = wb.sheetnames

# Write sheet names to a CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Sheet Names"])  # Write the header
    for sheet_name in sheet_names:
        csvwriter.writerow([sheet_name])  # Write each sheet name

print(f"CSV file created successfully at {csv_file_path}!")
