# Utilities

This project consists of a collection of utility scripts and modules, organized into different directories based on their functionality. Each
directory contains Python scripts that perform specific tasks.

## Directory Structure

The project is organized into the following directories:

- `Data_Operation`
- `Email_Operation`
- `File_Operation`
- `Kindle_Operation`
- `Media_Operation`
- `PDF_Operation`
- `Text_Operation`

### Data_Operation

This directory contains modules and scripts related to data operations. The following files are included:

- `_scrap_amazon.py`: Extracts product details from Amazon using provided URLs. (Details not finalised)
- `_scrap_shopee.py`: Extracts product details from Shopee using provided URLs. (Details not finalised)
- `download_youtube_mp3_from_txt.py`: Downloads YouTube videos as MP3 files using URLs from a text file.
- `download_youtube_mp4.py`: Downloads a single YouTube video as an MP4 file using a provided URL.
- `download_youtube_mp4_from_txt.py`: Downloads YouTube videos as MP4 files using URLs from a text file.

### Email_Operation

This directory contains modules and scripts related to email operations. The following files are included:

- `email_operation.py`: Offers a class for handling email operations such as logging in, data retrieval, email and attachment counting, and email
  processing.
- `count_email_files.py`: Utilizes the EmailOperation class to log into an email account, fetch and count emails and attachments, and then log out.
- `download_email_files.py`: Uses the EmailOperation class to log into an email account, fetch emails, download attachments with an optional renaming
  feature, and then log out.
- `email_search_error.py`: Establishes a custom exception for handling email search errors.

### File_Operation

This directory contains modules and scripts related to file operations. The following files are included:

- `check_docstring.py`: Scans Python files in a specified directory, checks for docstrings, and prints the file paths of those without docstrings.
- `copy_folder.py`: Copies a selected folder and its contents, appending the current date and time to the copied folder's name.
- `count_file_size_by_type_in_folder.py`: Calculates the total size of files of a specific type in a folder.
- `create_folders_in_folder.py`: Creates a new folder with a specified name within a given folder.
- `csv_populate_word.py`: Fills a Word template document with data from a CSV file, replacing placeholders with CSV values.
- `delete_empty_folders_in_folder.py`: Removes all empty directories in a specified path.
- `delete_empty_folders_in_folder_with_rename_index.py`: Deletes all empty directories and renames the remaining directories in a specified path.
- `draw_folder_structure.py`: Illustrates the structure of a specified folder.
- `extract_copy_files_in_folder.py`: Copies files with specified keywords from a directory to a destination directory.
- `extract_delete_files_in_folder.py`: Deletes files with specified keywords in a directory.
- `file_operation.py`: Provides various file operations including reading and writing text files, validating file paths, converting Word documents to
  PDF, and renaming files in a folder.
- `list_file_in_csv.py`: Lists all files in a specified directory and writes their full path, file name, and extension into a CSV file in the same
  directory.
- `manage_files_in_folder.py`: Moves files containing specified keywords to corresponding subdirectories in a specified directory.
- `move_folder_to_subfolder_count.py`: Moves files from a specified folder to newly created subfolders, ensuring a maximum file count in each
  subfolder.
- `move_folder_to_subfolder_size.py`: Moves folders from a specified directory to newly created subfolders, ensuring the total size of the folders in
  each subfolder does not exceed a specified maximum size.
- `move_subfolder_to_folder.py`: Moves all files from a specified subfolder to its parent folder, removing the subfolder if it's empty after the move.
- `read_write_text.py`: Reads a text file and overwrites it with a specified text input.
- `rename_files_in_folder.py`: Renames all files in a given folder based on user-specified patterns and modifications.
- `rename_files_in_folder2.py`: Copies files from one folder to another and renames them based on user-specified patterns and modifications.
- `unzip_archive_in_folder.py`: Unzips .zip and .rar archives in a directory.
- `word_to_pdf_in_folder.py`: Converts Word documents to PDF in a selected folder.

### Kindle_Operation

This directory contains modules and scripts related to Kindle operations. The following files are included:

- `kindle_operation.py`: Contains a class that includes various operations related to Kindle.
- `kindle_notes_html_to_md.py`: Converts Kindle notes from HTML to Markdown.

### Media_Operation

This directory contains modules and scripts related to media operations. The following files are included:

- `_add_photo_filter.py`: Adjusts image brightness based on average brightness, reading from an input folder and saving adjusted images to an output
  folder. (Details not finalised)
- `_add_title_overlay_moviepy.py`: Adds a title overlay to the first frame of a video using MoviePy, handling exceptions and logging errors. (Details
  not finalised)
- `batch_create_images_with_text_overlay.py:` Overlays text on images from input lists, allowing customization of font, size, color, and position.
- `crop_image_to_pieces.py:` Crops an image into a square and splits it into smaller squares, also includes a function to convert jpg images to png.
- `get_video_info.py:` Iterates over .mp4 files in a directory, retrieves their dimensions, and identifies videos with dimensions below a certain
  threshold.

### PDF_Operation

This directory contains modules and scripts related to PDF operations. The following files are included:

- `pdf_operation.py`: Manages PDF files, performing operations like deleting pages, rotating pages, extracting text, checking string presence,
  extracting titles, and compressing using PyPDF2 and pikepdf libraries.
- `pdf_operation_test.py`: Contains unit tests for the pdf_operation module, testing operations like deleting pages, rotating pages, and checking
  string presence using the unittest module and PyPDF2 library.
- `compress_pdf_ilovepdf.py`: Compresses a user-selected PDF file using the iLovePDF API.
- `compress_pdf_in_folder_ilovepdf.py`: Compresses all PDF files in a user-selected directory using the iLovePDF API.
- `compress_pdf_in_folder_ilovepdf_by_parts.py`: Compresses all PDF files in a user-selected directory in parts using the iLovePDF API.
- `compress_pdf_old_ilovepdf.py`: Compresses old PDF files in a user-selected directory using the iLovePDF API.
- `delete_pdf_page.py`: Removes a specific page from a user-selected PDF file.
- `delete_pdf_page_in_folder.py`: Removes a specific page from all PDF files in a user-selected directory.
- `extract_page_from_pdf_contain_keywords.py`: Extracts pages containing specific keywords from a user-selected PDF file.
- `extract_text_from_pdf.py`: Extracts text from a user-selected PDF file.
- `extract_title_from_pdf.py`: Extracts the title from a user-selected PDF file.
- `find_old_pdf.py`: Identifies and returns paths of old PDF files in a user-selected directory.
- `replace_old_pdf.py`: Replaces original PDF files with their compressed versions in a user-selected directory.
- `rotate_pdf.py`: Rotates a PDF file by a specific angle using the pdf_operation module and config settings.
- `rotate_pdf_in_folder.py`: Rotates all PDF files in a given folder by a specific angle using the pdf_operation module and config settings.

### Text_Operation

This directory contains modules and scripts related to text operations. The following files are included:

- `text_operation.py`: Contains a class that includes various operations related to text manipulation.
- `modify_text.py`: Modifies text based on specified rules.

## Usage

Each script can be run independently or run from the `main.py`. Please refer to the individual script files for specific usage instructions.

## Current Todo List

- Move similar code segments to the operation class module.
- Add more functionality and instructions in the main menu.
- Enable the user to input arguments in the main menu.