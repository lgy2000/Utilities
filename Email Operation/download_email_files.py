"""
Module name: download_email_files.py

Description:
Downloads email attachments from a specified email folder and save them to a local directory.
It also provides an option to rename the downloaded files based on the subject of the email.

Functions:
- save_attachment(part, filename, input_folder): Saves the email attachment to the specified directory.
- rename_file(filename, subject, require_original_filename): Renames the downloaded file based on the email subject.
- process_part(part, subject, require_original_filename, input_folder): Processes each part of the email message.
- process_attachments(email_address, password, email_folder, require_original_filename, input_folder): Logs into the email account, fetches emails,
processes each email, and logs out.
- main(email_address, password, email_folder, require_original_filename, input_folder): Calls the process_attachments function and prints a
completion message.

Notes:
- The module relies on the `get_email` module for logging into the email account and fetching email data.
- It also depends on the `quopri` library for decoding Quoted-Printable encoding in email headers.
- Email credentials, email folder path, input folder path, and renaming options are configured in the `config.py` file.
"""

import email
import os
import quopri

from email_search_error import email_search_error
from get_email import login_email, fetch_email_data, decode_header


def save_attachment(part, filename, input_folder):
    """
    Saves the email attachment to the specified directory.
    """
    save_path = os.path.join(input_folder, filename)
    with open(save_path, "wb") as f:
        f.write(part.get_payload(decode=True))
        print(f"Attachment '{filename}' saved successfully.")
    return save_path


def rename_file(filename, subject, require_original_filename):
    """
    Renames the downloaded file based on the email subject.
    """
    file_root, file_ext = os.path.splitext(filename)
    new_filename = f"{subject}{' ' + file_root if require_original_filename else ''}{file_ext}"
    return new_filename


def process_part(part, subject, require_original_filename, input_folder):
    """
    Processes each part of the email message.
    """
    if part.get_content_maintype() == "multipart":
        return
    if part.get("Content-Disposition") is None:
        return
    filename = decode_header(part.get_filename())
    filename = quopri.decodestring(filename).decode('utf-8')
    filename = os.path.basename(filename)
    if filename:
        save_path = save_attachment(part, filename, input_folder)
        new_filename = rename_file(filename, subject, require_original_filename)
        duplicate_counter = 1
        while os.path.isfile(os.path.join(input_folder, new_filename)):
            file_root, file_ext = os.path.splitext(new_filename)
            new_filename = f"{file_root} ({duplicate_counter}){file_ext}"
            duplicate_counter += 1
        os.rename(save_path, os.path.join(input_folder, new_filename))
        print(f"Renamed file to '{new_filename}'")


def process_attachments(email_address, password, email_folder, require_original_filename, input_folder):
    """
    Logs into the email account, fetches emails, processes each email, and logs out.
    """
    mail, result, data = login_email(email_address, password, email_folder)
    if result != "OK":
        raise email_search_error()
    for num in data[0].split():
        data = fetch_email_data(mail, num)
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = decode_header(msg["Subject"])
        print(f"Processing email with subject: {subject}")
        for part in msg.walk():
            process_part(part, subject, require_original_filename, input_folder)
    mail.logout()


def main(email_address, password, email_folder, require_original_filename, input_folder):
    process_attachments(email_address, password, email_folder, require_original_filename, input_folder)
    print(f"Finish downloading emails in folder: {email_folder}")


if __name__ == '__main__':
    from config import email_folder, input_folder, require_original_filename, email_address, password

    main(email_address, password, email_folder, require_original_filename, input_folder)
