import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(r"D:\YK\Python\Utilities\config.ini")

# Retrieve values from the configuration file
email_operation = 'EMAIL OPERATION'
email_address = config[email_operation]['email_address']
email_password = config[email_operation]['email_password']
email_folder = config[email_operation]['email_folder']
require_original_filename = config.getboolean(email_operation, 'require_original_filename')

file_operation = 'FILE OPERATION'
file_show_folder_dialog = config.getboolean(file_operation, 'show_folder_dialog')
file_show_file_dialog = config.getboolean(file_operation, 'show_file_dialog')
file_input_folder = config[file_operation]['input_folder']
file_input_file = config[file_operation]['input_file']

filename = config[file_operation]['filename']
list_of_placeholders = config[file_operation]['list_of_placeholders']

keyword = config[file_operation]['keyword']

input_text = config[file_operation]['input_text']
to_add_title = config.getint(file_operation, 'to_add_title')
to_remove_prefix = config.getint(file_operation, 'to_remove_prefix')
to_add_prefix = config.getint(file_operation, 'to_add_prefix')
to_add_suffix = config.getint(file_operation, 'to_add_suffix')
to_change_case = config.getint(file_operation, 'to_change_case')

rotation_angle = config.getint(file_operation, 'rotation_angle')

pdf_operation = 'PDF OPERATION'
pdf_show_folder_dialog = config.getboolean(pdf_operation, 'show_folder_dialog')
pdf_show_file_dialog = config.getboolean(pdf_operation, 'show_file_dialog')
pdf_input_folder = config[pdf_operation]['input_folder']
pdf_input_file = config[pdf_operation]['input_file']
page_number = config.getint(pdf_operation, 'page_number')
