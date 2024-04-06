"""
Module name: get_email.py

Description:
This module provides functions to connect to an email account via IMAP, select a specific email folder, search for emails, fetch email data,
and decode email headers.

Functions:
- login_email(email_address, password, email_folder): Logs into the email account, selects the specified email folder, and searches for all emails.
- fetch_email_data(mail, num): Fetches the raw data of a specific email.
- decode_header(header): Decodes an email header into a string.

Notes:
- The module uses the `imaplib` and `email` libraries for handling IMAP connections and email messages respectively.
- Email credentials and email folder path are passed as parameters to the functions.
"""

import email
import imaplib

from email_search_error import email_search_error


def login_email(email_address, password, email_folder):
    """
    Logs into the email account, selects the specified email folder, and searches for all emails.
    """
    # Connect to Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)

    # Select the folder containing the emails
    encoded_folder_name = email_folder.encode('utf-8')  # Encoding folder name to bytes
    mail.select(encoded_folder_name)

    # Search for emails with attachments
    result, data = mail.search(None, "ALL")

    return mail, result, data


def fetch_email_data(mail, num):
    """
    Fetches the raw data of a specific email.
    """
    result, data = mail.fetch(num, "(RFC822)")
    if result != "OK":
        raise email_search_error()
    return data


# Function to decode email header
def decode_header(header):
    """
    Decodes an email header into a string.
    """
    decoded_header = email.header.decode_header(header)
    decoded_str = []
    for decoded_part, encoding in decoded_header:
        if isinstance(decoded_part, bytes):
            decoded_str.append(decoded_part.decode(encoding or 'utf-8'))
        elif isinstance(decoded_part, str):
            decoded_str.append(decoded_part)
    return ''.join(decoded_str)
