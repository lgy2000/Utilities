#!/usr/bin/env python3

import configparser
import glob
import os
import re
import shutil
import time
import zipfile
from fnmatch import fnmatch
from pathlib import Path
from tkinter import filedialog

from pylovepdf.ilovepdf import ILovePdf

# Define constants
compress_level = 'compress'  # low, compress, extreme
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ALL_PDFS_PATTERN = "*.pdf"
COMPRESSED_PDFS_PATTERN = "*compress*.pdf"
COMPRESSED_ZIP_PATTERN = "*compress*.zip"
REGEX_ADDED_COMPRESSED_FILE_NAME = r"_compress_\d\d\-\d\d\-\d\d\d\d"

# Initialize lists and strings
pdf_files = []
compressed_pdfs = []
output_errors = ""

# Read the configuration file to get the public key
config = configparser.ConfigParser()
config.read(r"..\config.ini")
public_key = config['ILOVEPDF_USER_INFO']['PUBLIC_KEY']

# Ask the user to select a directory
ACTION_PATH = filedialog.askdirectory()

# Walk through the directory to find all PDF files
for path, subdirs, files in os.walk(ACTION_PATH):
    for name in files:
        if fnmatch(name, ALL_PDFS_PATTERN):
            pdf_files.append(os.path.join(path, name))

# Initialize the ILovePdf object and create a new task
ilovepdf = ILovePdf(public_key, verify_ssl=True)
task = ilovepdf.new_task(compress_level)

# Define the parent path
PARENT_PATH = os.path.dirname(ACTION_PATH)
print(f"Parent path: {PARENT_PATH}")

# Upload all the PDF files to the task
for file in pdf_files:
    print("Uploading: " + file)
    task.add_file(file)
    task.set_output_folder(PARENT_PATH)
    task.file.set_metas('Title', file)

# Execute the task, download the result, and delete the task
task.execute()
task.download()
task.delete_current_task()

# Wait for the task to finish
time.sleep(3)

# Unzip the downloaded compressed PDF files
zip_file_location = glob.glob(PARENT_PATH + "/" + COMPRESSED_ZIP_PATTERN)[0]
with zipfile.ZipFile(zip_file_location, 'r') as zip_ref:
    zip_ref.extractall(PARENT_PATH)
# print(f"Zip file location: {zip_file_location}")

# Wait for the extraction to finish
time.sleep(3)

# Find all the compressed PDFs recursively
compressed_pdfs = glob.glob(os.path.join(ACTION_PATH, '**', COMPRESSED_PDFS_PATTERN), recursive=True)
# print(f"Compressed PDFs: {compressed_pdfs}")

# Replace the recently compressed files to their original file location
for original_file in pdf_files:
    for compressed in compressed_pdfs:
        compressed_file = re.sub(
            REGEX_ADDED_COMPRESSED_FILE_NAME, '', compressed)
        if compressed_file[compressed_file.rindex("/")::] in original_file:
            if os.path.exists(Path(original_file).resolve()) and os.path.exists(Path(compressed).resolve()):
                print("Replacing: \t" + compressed + "\nto: \t\t" + original_file)
                shutil.move(Path(compressed), Path(original_file))
            else:  # file couldn't be replaced
                output_errors += "\n\033[1;31;40mError:\033[0m Couldn't replace: " + \
                                 compressed + " to " + original_file + '\n'

# If there are errors, print them all together
if len(output_errors) > 0:
    print("\n\033[91mFILES THAT COULDN'T BE REPLACED AND THEY MANUALLY HAVE TO BE REPLACED\033[0m")
    print(output_errors)

# Delete the zip file
os.remove(zip_file_location)
