import fnmatch
import os


def extract_files_with_keywords(directory, keywords):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for keyword in keywords:
                if fnmatch.fnmatch(file.lower(), f'*{keyword.lower()}*'):
                    source_file_path = os.path.join(root, file)
                    matching_files.append(source_file_path)
                    print(source_file_path)
                    os.remove(source_file_path)
    return matching_files


def main():
    keywords = [".zip", ".rar"]
    directory = r"D:\YK\Honeywell\2023 MYP-000302 RESET MRCSB\WP126 PU\Transmittal 2024.4.18"
    extract_files_with_keywords(directory, keywords)


if __name__ == "__main__":
    main()
