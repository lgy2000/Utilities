# !/usr/bin/env python3

"""
config.py

This module is used for handling configuration settings for the application.

Description:
This module uses the configparser library to read configuration settings from a .ini file. It provides easy access to these settings throughout the
application, including settings related to email operations, file operations, and PDF operations.
"""

import configparser
import os

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'config.ini')  # Construct the full path to the config.ini file
config.read(config_file_path)  # Use the full path as the argument

# Retrieve values from the configuration file
email_operation = 'EMAIL OPERATION'
email_address = config[email_operation]['email_address']
email_password = config[email_operation]['email_password']
email_folder = config[email_operation]['email_folder']
require_original_filename = config.getboolean(email_operation, 'require_original_filename')

data_operation = 'DATA OPERATION'
email_address_heroic = config[data_operation]['email_address_heroic']
email_password_heroic = config[data_operation]['email_password_heroic']
email_address_ios_calendar = config[data_operation]['email_address_ios_calendar']
email_password_ios_calendar = config[data_operation]['email_password_ios_calendar']

file_operation = 'FILE OPERATION'
file_allowed_paths = config[file_operation]['allowed_paths'].split('"')
file_allowed_paths = [item for item in file_allowed_paths if item != '']
file_show_folder_dialog = config.getboolean(file_operation, 'show_folder_dialog')
file_show_file_dialog = config.getboolean(file_operation, 'show_file_dialog')
file_input_folder = config[file_operation]['input_folder']
file_input_file = config[file_operation]['input_file']

filename = config[file_operation]['filename']
filename_placeholders = config[file_operation]['filename_placeholders']
list_of_placeholders = config[file_operation]['list_of_placeholders'].split(',')

input_text = config[file_operation]['input_text']
add_title = config.getint(file_operation, 'add_title')
remove_prefix = config.getint(file_operation, '_remove_prefix')
to_add_prefix = config.getint(file_operation, 'to_add_prefix')
to_add_suffix = config.getint(file_operation, 'to_add_suffix')
to_change_case = config.getint(file_operation, 'to_change_case')

rotation_angle = config.getint(file_operation, 'rotation_angle')

pdf_operation = 'PDF OPERATION'
pdf_show_folder_dialog = config.getboolean(pdf_operation, 'show_folder_dialog')
pdf_show_file_dialog = config.getboolean(pdf_operation, 'show_file_dialog')
pdf_input_folder = config[pdf_operation]['input_folder']
pdf_input_file = config[pdf_operation]['input_file']
pdf_page_number = config.getint(pdf_operation, 'page_number')

text_operation = 'TEXT OPERATION'
text_title_keyword = config[text_operation]['title_keyword']
text_prefix_str = config[text_operation]['prefix_str']
text_suffix_str = config[text_operation]['suffix_str']

#
#
# config = {
#     'csv_populate_word': {
#         'filename': 'filename',
#         'list_of_placeholders': ["tpno", "tagno"],
#     },
#     'modify_text': {
#         'input_text': 'input input',
#         'filename': 'another_filename',
#     },
#     'rotate_pdf': {
#         'rotation_angle': 270,
#         'filename': 'yet_another_filename',
#     },
#     # and so on for the other scripts...
# }
