import os
import re


def add_prefix_to_filenames(directory, prefix):
    # List all files in the specified directory
    for filename in os.listdir(directory):
        # Define the regex pattern to match the beginning of the filename
        pattern = r'^(.*)$'

        # Replace the match with the prefix and the original filename
        new_filename = re.sub(pattern, fr'{prefix}\1', filename)

        # Construct full file paths
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed "{filename}" to "{new_filename}"')


# Example usage
directory = r"D:\YK\Downloads\heroic1 - Copy"  # Replace with your directory path
prefix = r"Philosopher's Note Summary - "  # Replace with your desired prefix
add_prefix_to_filenames(directory, prefix)
