# !/usr/bin/env python3

"""
categorize_files_in_folder.py

This module is used for categorizing files in a directory based on keywords.

Description:
This module contains a function that iterates over all files in a specified directory. If a file's name contains any of the provided keywords,
the file is moved to a corresponding subdirectory. The subdirectories are created based on the keywords.
"""

import os
import shutil


def manage_files_in_folder(path, keywords):
    # Create folders for each keyword in the given path
    for i, keyword in enumerate(keywords, start=1):
        os.makedirs(os.path.join(path, f"{i} {keyword.title()}"), exist_ok=True)

    # Iterate over all files in the given path
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check if the filename contains any of the keywords
        for i, keyword in enumerate(keywords, start=1):
            if keyword.lower() in filename.lower():
                # Move the file to the corresponding folder
                shutil.move(file_path, os.path.join(path, f"{i} {keyword}", filename))
                break  # If a file is moved, no need to check other keywords


def main():
    path = r"E:\All\7 Media\7.7 Fitness\Video"
    keywords = ["Meditation", "full", "abs", "back", "arm", "shoulder", "upper", "lower", "leg", "thigh", "butt", "aerobic", "Cardio", "HIIT",
                "Stretch", "Yoga", "Pilates", "Tabata"]
    manage_files_in_folder(path, keywords)


if __name__ == "__main__":
    main()
