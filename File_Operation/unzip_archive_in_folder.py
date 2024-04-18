import os
import zipfile

import rarfile


def unzip_archives_in_folder(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                print(type(file_path))
                print(type('r'))
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
            elif file.endswith('.rar'):
                file_path = os.path.join(root, file)
                with rarfile.RarFile(file_path, 'r') as rar_ref:
                    rar_ref.extractall(root)


def main():
    unzip_archives_in_folder(r"D:\YK\Downloads\TRANSMITTAL2")


if __name__ == "__main__":
    main()
