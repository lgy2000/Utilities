"""
email_operation.py

Handles email operations such as downloading attachments and counting emails.

Description:
This module provides functions for various email operations such as downloading attachments from a specified email folder and counting the number
of emails and attachments in a specified email folder. It relies on other modules like `download_email_files.py` and `count_email_files.py` for
specific operations.
"""

import email
import imaplib
import os
import quopri

from email_search_error import EmailSearchError


class EmailOperation:
    def __init__(self):
        # No initialization required
        pass

    @staticmethod
    def login_email(email_address, password, email_folder):
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)

        # Select the folder containing the emails
        encoded_folder_name = email_folder.encode('utf-8')  # Encoding folder name to bytes
        mail.select(encoded_folder_name)

        # Search for emails with attachments
        result, data = mail.search(None, "ALL")

        return mail, result, data

    @staticmethod
    def fetch_email_data(mail, num):
        """
        Fetches the raw data of a specific email.
        """
        result, data = mail.fetch(num, "(RFC822)")
        if result != "OK":
            raise EmailSearchError()
        return data

    @staticmethod
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

    @staticmethod
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

    def count_emails_and_attachments(self, email_address, password, email_folder):
        """
        Logs into the email account, fetches emails, counts the number of emails and attachments, and logs out.
        """
        mail, result, data = self.login_email(email_address, password, email_folder)
        if result != "OK":
            raise EmailSearchError()
        email_count = len(data[0].split())
        attachment_count = 0
        for num in data[0].split():
            data = self.fetch_email_data(mail, num)
            raw_email = data[0][1]
            attachment_count += self.count_attachments_in_email(raw_email)
        mail.logout()
        return email_count, attachment_count

    @staticmethod
    def save_attachment(part, filename, input_folder):
        """
        Saves the email attachment to the specified directory.
        """
        save_path = os.path.join(input_folder, filename)
        with open(save_path, "wb") as f:
            f.write(part.get_payload(decode=True))
            print(f"Attachment '{filename}' saved successfully.")
        return save_path

    @staticmethod
    def _rename_file(filename, subject, require_original_filename):
        """
        Renames the downloaded file based on the email subject.
        """
        file_root, file_ext = os.path.splitext(filename)
        new_filename = f"{subject}{' ' + file_root if require_original_filename else ''}{file_ext}"
        return new_filename

    def process_part(self, part, subject, require_original_filename, input_folder):
        """
        Processes each part of the email message.
        """
        if part.get_content_maintype() == "multipart":
            return
        if part.get("Content-Disposition") is None:
            return
        filename = self.decode_header(part.get_filename())
        filename = quopri.decodestring(filename).decode('utf-8')
        filename = os.path.basename(filename)
        if filename:
            save_path = self.save_attachment(part, filename, input_folder)
            new_filename = self._rename_file(filename, subject, require_original_filename)
            duplicate_counter = 1
            while os.path.isfile(os.path.join(input_folder, new_filename)):
                file_root, file_ext = os.path.splitext(new_filename)
                new_filename = f"{file_root} ({duplicate_counter}){file_ext}"
                duplicate_counter += 1
            os.rename(save_path, os.path.join(input_folder, new_filename))
            print(f"Renamed file to '{new_filename}'")

    def process_emails_and_attachments(self, email_address, email_password, email_folder, require_original_filename, input_folder):
        """
        Logs into the email account, fetches emails, processes each email, and logs out.
        """
        mail, result, data = self.login_email(email_address, email_password, email_folder)
        if result != "OK":
            raise EmailSearchError()
        for num in data[0].split():
            data = self.fetch_email_data(mail, num)
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = self.decode_header(msg["Subject"])
            print(f"Processing email with subject: {subject}")
            for part in msg.walk():
                self.process_part(part, subject, require_original_filename, input_folder)
        mail.logout()
