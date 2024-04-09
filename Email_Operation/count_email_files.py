"""
count_email_files.py

Counts the number of emails and attachments in a specified email folder.

Description:
This module logs into the email account, fetches emails, counts the number of emails and attachments, and logs out. It relies on the `get_email`
module for logging into the email account and fetching email data, and the `email` library for parsing email messages. Email credentials and email
folder path are configured in the `config.py` file.
"""

from email_operation import EmailOperation


def main(_email_address, _email_password, _email_folder):
    """
    Calls the count_emails_and_attachments function and prints the results.
    """
    try:
        email_ops = EmailOperation()
        email_count, attachment_count = email_ops.count_emails_and_attachments(_email_address, _email_password, _email_folder)
        print(f"Number of emails in folder '{_email_folder}': {email_count}")
        print(f"Total number of attachments in folder '{_email_folder}': {attachment_count}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    from config import email_folder, email_address, email_password

    main(email_address, email_password, email_folder)
