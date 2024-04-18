import fnmatch
import os
import shutil


def extract_files_with_keywords(directory, keywords, destination_directory):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for keyword in keywords:
                if fnmatch.fnmatch(file, f'*{keyword}*'):
                    source_file_path = os.path.join(root, file)
                    matching_files.append(source_file_path)
                    print(source_file_path)
                    shutil.copy2(source_file_path, str(destination_directory))
    return matching_files


def main():
    keywords = ["WPR"]
    directory = r"D:\YK\Downloads\TRANSMITTAL_UNZIPPED"
    destination_directory = r"D:\YK\Downloads\REP_WPR"
    extract_files_with_keywords(directory, keywords, destination_directory)


if __name__ == "__main__":
    main()
