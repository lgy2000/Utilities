# !/usr/bin/env python3

"""
csv_populate_word.py

Populates a Word template document with data from a CSV file.

Description:
This module provides a function to populate a Word template document with data from a CSV file. It replaces placeholders in the template with
values from each row of the CSV. It utilizes the pandas and docx modules for data manipulation and Word document operations respectively.

Note:
Must save as CSV UTF-8.
"""

import sys
import traceback

from eglogging import logging_load_human_config, CRITICAL

# from config import filename, list_of_placeholders
from file_operation import FileOperation

logging_load_human_config()


def main():
    try:
        file_ops = FileOperation()
        file_ops.csv_populate_word(filename, list_of_placeholders)
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    list_of_placeholders = ['DEV_ID', 'PHASE', 'CAT', 'COMPONENTS', 'SPECIFICATION', 'DEVIATION_DESCRIPTION', 'REQUIRED_REMEDIAL_ACTIONS',
                            'ACTUAL_DEVELOPMENT_ACTIONS', 'SUBMITTER', 'SUBMIT_DATE']
    filename = list_of_placeholders[0]
    main()
