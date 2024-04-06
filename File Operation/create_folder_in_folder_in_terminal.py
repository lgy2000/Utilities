import os
import sys

def create_folders(folder, folder_names):
    for folder_name in folder_names:
        if not folder_name:
            continue  # Skip empty lines
        try:
            folder_path = os.path.join(folder, folder_name)
            os.makedirs(folder_path)
            print(f"Successfully created folder '{folder_name}'.")
        except OSError as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python create_folders.py <folder_path> <folder_name1> <folder_name2> ...")
        sys.exit(1)

    folder = sys.argv[1]
    folder_names = sys.argv[2:]
    create_folders(folder, folder_names)

if __name__ == "__main__":
    main()
