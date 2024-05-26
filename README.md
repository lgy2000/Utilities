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

- `_scrap_amazon.py`: Scrapes product information from Amazon. The product URLs are provided as inputs. (Details not finalised)
- `_scrap_shopee.py`: Scrapes product information from Shopee. The product URLs are provided as inputs. (Details not finalised)
- `download_youtube_mp3_from_txt.py`: Downloads YouTube videos as MP3 files. The URLs of the videos are read from a text file.
- `download_youtube_mp4.py`: Downloads a YouTube video as an MP4 file. The URL of the video is provided as an input.
- `download_youtube_mp4_from_txt.py`: Downloads YouTube videos as MP4 files. The URLs of the videos are read from a text file.

### Email_Operation

This directory contains modules and scripts related to email operations. The following files are included:

- `email_operation.py`: Contains a class that includes various operations related to emails.
- `count_email_files.py`: Counts the number of email files.
- `download_email_files.py`: Downloads email files.
- `email_search_error.py`: Handles email search errors.

### File_Operation

This directory contains modules and scripts related to file operations. The following files are included:

check_docstring.py: Scans all Python files in a specified directory and checks if they have a docstring. Prints the file paths of those files that do
not have a docstring.
copy_folder.py: Copies a folder.
count_file_size_by_type_in_folder.py: Counts the total size of files of a specific type in a folder.
create_folders_in_folder.py: Creates multiple folders within a folder.
csv_populate_word.py: Populates a Word document with data from a CSV file.
delete_empty_folders_in_folder.py: Deletes all empty folders in a specified directory.
delete_empty_folders_in_folder_with_rename_index.py: Deletes all empty folders in a specified directory and renames the index of remaining folders.
draw_folder_structure.py: Draws the structure of a specified directory.
extract_copy-files—in_folder.py: Copies files from a specified directory.
extract_delete_files_in_folder.py: Deletes files from a specified directory.

### Kindle_Operation

This directory contains modules and scripts related to Kindle operations. The following files are included:

- `kindleoperation.py`: Contains a class that includes various operations related to Kindle.
- `kindle_notes_html_to_md.py`: Converts Kindle notes from HTML to Markdown.

### Media_Operation

This directory contains modules and scripts related to media operations. The following files are included:

- `_add_photo_filter.py`: Applies a filter to a photo. (Details not finalised)
- `_add_title_overlay_moviepy.py`: Adds a title overlay to a video using the MoviePy library. (Details not finalised)
- `batch_create_images_with_text_overlay.py`: Creates multiple images with text overlay in a batch process.
- `crop_image_to_pieces.py`: Crops an image into multiple pieces.
- `get_video_info.py`: Retrieves information about a video file.

### PDF_Operation

This directory contains modules and scripts related to PDF operations. The following files are included:

- `pdf_operation.py`: Contains a class that includes various operations related to PDF files.
- `compress_pdf_ilovepdf.py`: Compresses a PDF file using the iLovePDF service.
- `compress_pdf_in_folder_ilovepdf.py`: Compresses all PDF files in a specified directory using the iLovePDF service.
- `compress_pdf_in_folder_ilovepdf_by_parts.py`: Compresses all PDF files in a specified directory by parts using the iLovePDF service.
- `compress_pdf_old_ilovepdf.py`: Compresses an old PDF file using the iLovePDF service.
- `delete_pdf_page.py`: Deletes a specific page from a PDF file.
- `delete_pdf_page_in_folder.py: Deletes a specific page from all PDF files in a specified directory.
- `extract-page`-from_pdf_contain_keywords.py: Extracts pages from a PDF file that contain specific keywords.
- `extract-text`-from-pdf.py: Extracts text from a PDF file.
- `extract-title`-from-pdf.py: Extracts the title from a PDF file.
- `find_old-pdf`.py: Finds old PDF files in a specified directory.
- `pdf_operation_test.py`: Contains tests for the pdf_operation.py module.
- `replace_old_pdf.py`: Replaces old PDF files with new ones in a specified directory.
- `rotate-pdf`.py: Rotates a PDF file by a specified angle.
- `rotate_pdf-in`-folder.py: Rotates all PDF files in a specified directory by a specified angle.

### Text_Operation

This directory contains modules and scripts related to text operations. The following files are included:

- `text_operation.py`: Contains a class that includes various operations related to text manipulation.
- `modify_text.py`: Modifies text based on specified rules.

## Usage

Each script can be run independently or run from the `main_menu.py`. Please refer to the individual script files for specific usage instructions.

## Current Todo List

- Move similar code segments to the operation class module.
- Add more functionality and instructions in the main menu.
- Enable the user to input arguments in the main menu.