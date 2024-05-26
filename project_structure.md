```
Utilities
│   .gitattributes
│   .gitignore
│   config.ini
│   config.py
│   desktop.ini
│   main.py
│       ['get_callable_functions', 'list_python_files', 'execute_script', 'main_menu', 'again', 'main']
│   project_structure.md
│   README.md
│   __init__.py
│   
├───Data_Operation
│   │   download_youtube_mp3_from_txt.py
│   │       ['download_youtube', 'main']
│   │   download_youtube_mp4.py
│   │       ['download_youtube', 'main']
│   │   download_youtube_mp4_from_txt.py
│   │       ['main']
│   │   _scrap_amazon.py
│   │   _scrap_shopee.py
│   │   __init__.py
│   │   
│   ├───Youtube Transcript API
│   │   │   .coveragerc
│   │   │   .travis.yml
│   │   │   coverage.sh
│   │   │   README.md
│   │   │   setup.py
│   │   │       ['_get_file_content', 'get_long_description', 'get_test_suite']
│   │   │   youtube_transcript.py
│   
├───Email_Operation
│   │   count_email_files.py
│   │       ['main']
│   │   download_email_files.py
│   │       ['main']
│   │   email_operation.py
│   │       ['__init__', 'login_email', 'fetch_email_data', 'decode_header', 'count_attachments_in_email', 'count_emails_and_attachments', 'save_attachment', '_rename_file', 'process_part', 'process_emails_and_attachments']
│   │   email_search_error.py
│   │       ['__init__']
│   │   __init__.py
│   
├───File_Operation
│   │   check_docstring.py
│   │       ['has_docstring', 'main']
│   │   copy_folder.py
│   │       ['main']
│   │   count_file_size_by_type_in_folder.py
│   │       ['count_file_size_by_type_in_folder', 'main']
│   │   create_folders_in_folder.py
│   │       ['main']
│   │   csv_populate_word.py
│   │       ['main']
│   │   delete_empty_folders_in_folder.py
│   │       ['delete_empty_folders', 'main']
│   │   delete_empty_folders_in_folder_with_rename_index.py
│   │       ['delete_empty_folders_and_rename', 'main']
│   │   draw_folder_structure.py
│   │       ['get_callable_functions', 'calculate_indent', 'print_with_indent', 'print_callable_functions', 'draw_directory_structure', 'main']
│   │   extract_copy_files_in_folder.py
│   │       ['extract_files_with_keywords', 'main']
│   │   extract_delete_files_in_folder.py
│   │       ['extract_files_with_keywords', 'main']
│   │   file_operation.py
│   │       ['__init__', 'get_current_folder_path', 'get_parent_folder_path', 'copy_folder_structure', 'copy_folder_and_files', 'create_folders_in_folder', 'select_folder_word_csv', 'csv_populate_word', 'is_filepath_valid', 'read_write_txt', 'word_to_pdf_in_folder', 'rename_file_in_folder']
│   │   list_file_in_csv.py
│   │       ['list_files_to_csv']
│   │   manage_files_in_folder.py
│   │       ['manage_files_in_folder', 'main']
│   │   move_folder_to_subfolder_count.py
│   │       ['move_folder_to_subfolder', 'main']
│   │   move_folder_to_subfolder_size.py
│   │       ['get_folder_size', 'move_folder_to_subfolder', 'main']
│   │   move_subfolder_to_folder.py
│   │       ['move_subfolder_to_folder', 'main']
│   │   read_write_text.py
│   │       ['main']
│   │   rename_files_in_folder.py
│   │       ['get_test_folder', 'get_user_input', 'main']
│   │   rename_files_in_folder2.py
│   │       ['get_test_folder', 'to_uppercase', 'parse_command_line_args', 'get_user_input', 'main']
│   │   unzip_archive_in_folder.py
│   │       ['unzip_archives_in_folder', 'main']
│   │   word_to_pdf_in_folder.py
│   │       ['main']
│   │   __init__.py
│   
├───Kindle_Operation
│   │   kindle_notes_html_to_md.py
│   │       ['get_test_file', 'parse_command_line_args', 'get_user_input', 'main']
│   │   kindle_notes_html_to_md_README.md
│   │   kindle_notes_html_to_md_screenshot.png
│   │   kindle_operation.py
│   │       ['__init__', '__init__', 'get_last_note', '__init__', 'parse_file', '_read_parse_file', '_get_all_divs', '_process_divs', '_process_note_heading', '_process_note_text', 'output_md', '_create_md_header', '_create_md_body', '_output_markdown_to_destination', '_get_book_info', '_extract_notes_only', '_extract_highlights_only', '_format_notes']
│   │   __init__.py
│   
├───Media_Operation
│       batch_create_images_with_text_overlay.py
│           ['get_date_today', 'batch_create_images_with_text_overlay', 'main']
│       crop_image_to_pieces.py
│           ['convert_jpg_to_png', 'is_square', 'crop_to_square', 'split_image', 'process_image', 'main']
│       get_video_info.py
│           ['get_video_info', 'main']
│       _add_photo_filter.py
│           ['calculate_average_brightness', 'adjust_brightness', 'main']
│       _add_title_overlay_moviepy.py
│           ['add_title_overlay', 'main']
│       __init__.py
│   
├───PDF_Operation
│   │   compress_pdf_ilovepdf.py
│   │       ['main']
│   │   compress_pdf_in_folder_ilovepdf.py
│   │       ['main']
│   │   compress_pdf_in_folder_ilovepdf_by_parts.py
│   │       ['main']
│   │   compress_pdf_old_ilovepdf.py
│   │       ['main']
│   │   delete_pdf_page.py
│   │       ['main']
│   │   delete_pdf_page_in_folder.py
│   │       ['main']
│   │   extract_page_from_pdf_contain_keywords.py
│   │       ['extract_page_from_pdf_contain_keywords', 'main']
│   │   extract_text_from_pdf.py
│   │       ['extract_text_from_pdf', 'is_in_list', 'main']
│   │   extract_title_from_pdf.py
│   │       ['main']
│   │   find_old_pdf.py
│   │       ['main']
│   │   pdf_operation.py
│   │       ['__init__', 'get_current_folder_path', 'get_parent_folder_path', 'delete_pdf_page', 'delete_pdf_page_in_folder', 'rotate_pdf_page', 'rotate_pdf', 'rotate_pdf_in_folder', 'check_pdf_rotation', 'is_string_in_pdf', 'get_text_from_pdf', 'extract_title_from_pdf', 'compress_pdf_folder_ilovepdf', 'compress_pdf_file_ilovepdf']
│   │   pdf_operation_test.py
│   │       ['main', 'setUp', 'test_delete_pdf_page_1', 'test_rotate_pdf']
│   │   replace_old_pdf.py
│   │       ['main']
│   │   rotate_pdf.py
│   │       ['main']
│   │   rotate_pdf_in_folder.py
│   │       ['main']
│   │   __init__.py
│   │   
│   ├───Compress-PDFs
│   │   │   .env
│   │   │   .env.example
│   │   │   .gitignore
│   │   │   compress.py
│   │   │   LICENSE
│   │   │   MAKE_SCRIPT_GLOBAL.sh
│   │   │   README.md
│   │   
│   ├───cpdf-binaries-master
│   │   │   cpdfmanual.pdf
│   │   │   LICENSE
│   │   │   README.md
│   │   │   
│   │   ├───Linux-Intel-64bit
│   │   │       cpdf
│   │   │   
│   │   ├───old32bit
│   │   │   │   
│   │   │   ├───Linux-Intel-32bit
│   │   │   │       cpdf
│   │   │   
│   │   ├───OSX-ARM
│   │   │       cpdf
│   │   │   
│   │   ├───OSX-Intel
│   │   │       cpdf
│   │   │   
│   │   ├───Windows32bit
│   │   │       cpdf.exe
│   │   │   
│   │   ├───Windows64bit
│   │   │       cpdf.exe
│   
├───Text_Operation
│   │   modify_text.py
│   │       ['main']
│   │   text_operation.py
│   │       ['__init__', '__init__', 'set_args', 'print_args', 'process_text', 'clean_string', 'get_title_from_text', '_remove_prefix', 'get_prefix', 'get_suffix', 'change_case', 'get_title_case']
│   │   __init__.py
```