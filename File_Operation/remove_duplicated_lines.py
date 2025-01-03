def remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove duplicates by converting the list to a set, then convert it back to a list
    lines = list(set(lines))
    # Sort the lines
    lines = sorted(lines)
    with open(file_path, 'w') as file:
        file.writelines(lines)


def main():
    file_path = r"D:\YK\Python\Utilities\Data_Operation\Existing Links.txt"  # Replace with your file path
    remove_duplicates(file_path)


if __name__ == "__main__":
    main()
