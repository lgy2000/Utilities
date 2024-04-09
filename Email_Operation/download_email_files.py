"""
download_email_files.py

Downloads email attachments from a specified email folder and save them to a local directory.

Description:
This module logs into the email account, fetches emails, downloads attachments, and logs out. It also provides an option to rename the downloaded
files based on the subject of the email. It relies on the `get_email` module for logging into the email account and fetching email data,
and the `quopri` library for decoding Quoted-Printable encoding in email headers. Email credentials, email folder path, input folder path,
and renaming options are configured in the `config.py` file.
"""

from email_operation import EmailOperation


def main(_email_address, _email_password, _email_folder, _require_original_filename, _input_folder):
    email_ops = EmailOperation()
    email_ops.process_emails_and_attachments(_email_address, _email_password, _email_folder, _require_original_filename, _input_folder)
    print(f"Finish downloading emails in folder: {_email_folder}")


if __name__ == '__main__':
    from config import email_folder, file_input_folder, require_original_filename, email_address, email_password

    main(email_address, email_password, email_folder, require_original_filename, file_input_folder)
