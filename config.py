import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Retrieve values from the configuration file
email = config['EMAIL OPERATION']['email']
password = config['EMAIL OPERATION']['password']
email_folder = config['EMAIL OPERATION']['email_folder']
require_original_filename = config.getboolean('EMAIL OPERATION', 'require_original_filename')

show_folder_dialog = config.getboolean('FILE OPERATION', 'show_folder_dialog')
show_file_dialog = config.getboolean('FILE OPERATION', 'show_file_dialog')
input_folder = config['FILE OPERATION']['input_folder']
input_file = config['FILE OPERATION']['input_file']

filename = config['FILE OPERATION']['filename']
list_of_placeholders = config['FILE OPERATION']['list_of_placeholders']

page_number = config.getint('FILE OPERATION', 'page_number')

keyword = config['FILE OPERATION']['keyword']

input_text = config['FILE OPERATION']['input_text']
to_add_title = config.getint('FILE OPERATION', 'to_add_title')
to_remove_prefix = config.getint('FILE OPERATION', 'to_remove_prefix')
to_add_prefix = config.getint('FILE OPERATION', 'to_add_prefix')
to_add_suffix = config.getint('FILE OPERATION', 'to_add_suffix')
to_change_case = config.getint('FILE OPERATION', 'to_change_case')

rotation_angle = config.getint('FILE OPERATION', 'rotation_angle')
