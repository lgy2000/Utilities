"""
Module name: count_email_files.py

Description:
Counts the number of emails and attachments in a specified email folder.

Functions:
- count_attachments_in_email(raw_email): Counts the number of attachments in a given raw email data.
- count_emails_and_attachments(email_address, password, email_folder): Logs into the email account, fetches emails, counts the number of emails and
attachments, and logs out.
- main(email_address, password, email_folder): Calls the count_emails_and_attachments function and prints the results.

Notes:
- The module relies on the `get_email` module for logging into the email account and fetching email data.
- It also depends on the `email` library for parsing email messages.
- Email credentials and email folder path are configured in the `config.py` file.
"""

import email

from email_search_error import email_search_error
from get_email import login_email, fetch_email_data


def count_attachments_in_email(raw_email):
    """
    Counts the number of attachments in a given raw email data.
    """
    msg = email.message_from_bytes(raw_email)
    attachment_count = 0
    for part in msg.walk():
        if part.get_content_maintype() != "multipart" and part.get("Content-Disposition") is not None:
            attachment_count += 1
    return attachment_count


def count_emails_and_attachments(email_address, password, email_folder):
    """
    Logs into the email account, fetches emails, counts the number of emails and attachments, and logs out.
    """
    mail, result, data = login_email(email_address, password, email_folder)
    if result != "OK":
        raise email_search_error()
    email_count = len(data[0].split())
    attachment_count = 0
    for num in data[0].split():
        data = fetch_email_data(mail, num)
        raw_email = data[0][1]
        attachment_count += count_attachments_in_email(raw_email)
    mail.logout()
    return email_count, attachment_count


def main(email_address, email_password, email_folder):
    """
    Calls the count_emails_and_attachments function and prints the results.
    """
    try:
        email_count, attachment_count = count_emails_and_attachments(email_address, email_password, email_folder)
        print(f"Number of emails in folder '{email_folder}': {email_count}")
        print(f"Total number of attachments in folder '{email_folder}': {attachment_count}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    from config import email_folder, email_address, email_password

    main(email_address, email_password, email_folder)
