import pandas as pd
from datetime import datetime

def rename_excel_sheets(excel_file_path, mapping_file_path, error_file_path):
    """
    Renames sheets in an Excel file based on a mapping provided in another Excel file.
    """
    try:
        # Load the mapping file
        df = pd.read_excel(mapping_file_path, skiprows=0)
        # Drop rows with any missing values
        df = df.dropna(how='any').reset_index(drop=True)
        print("Mapping DataFrame after loading and cleaning:")
        print(df)
    except Exception as e:
        print(f"Error reading mapping file: {e}")
        return

    try:
        # Load the target Excel file
        excel_file = pd.ExcelFile(excel_file_path)
        print(f"Sheet names in target Excel file: {excel_file.sheet_names}")
    except Exception as e:
        print(f"Error reading target Excel file: {e}")
        return

    with open(error_file_path, 'a', encoding='utf-8') as error_file:
        sheet_rename_dict = {}
        used_sheet_names = set()

        # Build the rename dictionary
        for index, row in df.iterrows():
            old_sheet_name = row.iloc[0].strip()
            new_sheet_name = str(row.iloc[1]).strip()

            if old_sheet_name in excel_file.sheet_names:
                if new_sheet_name in used_sheet_names:
                    error_file.write(f"[{datetime.now()}] Duplicate sheet name: {new_sheet_name}\n")
                elif not is_valid_sheet_name(new_sheet_name):
                    error_file.write(f"[{datetime.now()}] Invalid sheet name: {new_sheet_name}\n")
                else:
                    sheet_rename_dict[old_sheet_name] = new_sheet_name
                    used_sheet_names.add(new_sheet_name)
            else:
                error_file.write(f"[{datetime.now()}] Sheet not found: {old_sheet_name}\n")

        print(f"Sheet rename dictionary: {sheet_rename_dict}")

        try:
            # Read all sheets into a dictionary
            excel_data = pd.read_excel(excel_file_path, sheet_name=None)

            # Write sheets to a new Excel file with renamed sheets
            with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
                for sheet_name, data in excel_data.items():
                    new_sheet_name = sheet_rename_dict.get(sheet_name, sheet_name)
                    print(f"Writing sheet: {sheet_name} as {new_sheet_name}")
                    data.to_excel(writer, sheet_name=new_sheet_name, index=False)
        except Exception as e:
            print(f"Error writing Excel file: {e}")

def is_valid_sheet_name(sheet_name):
    """
    Validates the sheet name for Excel.
    """
    invalid_chars = ['*', ':', '?', '[', ']', '/']
    return len(sheet_name) <= 31 and not any(char in sheet_name for char in invalid_chars)

def main():
    excel_file_path = r'D:\YK\Downloads\Book1.xlsx'
    mapping_file_path = r'D:\YK\Downloads\Book2.xlsx'
    error_file_path = r'D:\YK\Downloads\error.txt'
    rename_excel_sheets(excel_file_path, mapping_file_path, error_file_path)

if __name__ == "__main__":
    main()

