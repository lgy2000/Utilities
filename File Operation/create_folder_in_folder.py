import os
from tkinter import filedialog


def create_folders(folder):
    print("Enter folder names (press Enter to finish):")
    while True:
        folder_name = input().strip()
        if folder_name.upper() == 'Q':
            raise SystemExit
        if not folder_name:
            break  # Stop input loop if Enter is pressed
        try:
            folder_path = os.path.join(folder, folder_name)
            os.makedirs(folder_path)
            print(f"Created folder '{folder_name}'.")
        except OSError as e:
            print(f"Error: {e}")

def main():
    folder = filedialog.askdirectory()
    if folder:
        create_folders(folder)
    else:
        print("No folder selected.")


if __name__ == "__main__":
    main()
