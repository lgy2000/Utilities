"""
count_email_files.py

Description:
Count total number of files in an email folder

Notes:
- Input values for the configuration variables in config.py.

"""
import email

from config import email_folder
from get_email import login_email
from credentials import email_address, password

def count_emails_and_attachments(email_address, password, email_folder):
    mail, result, data = login_email(email_address, password, email_folder)

    if result == "OK":
        email_count = len(data[0].split())
        attachment_count = 0
        for num in data[0].split():
            result, data = mail.fetch(num, "(RFC822)")
            if result == "OK":
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                for part in msg.walk():
                    if part.get_content_maintype() != "multipart" and part.get("Content-Disposition") is not None:
                        attachment_count += 1
        return email_count, attachment_count
    else:
        print("Failed to search emails.")
        return None, None

    # Logout and close connection
    mail.logout()


def main():
    # Count emails and attachments
    email_count, attachment_count = count_emails_and_attachments(email_address, password, email_folder)
    if email_count is not None and attachment_count is not None:
        print(f"Number of emails in folder '{email_folder}': {email_count}")
        print(f"Total number of attachments in folder '{email_folder}': {attachment_count}")
    else:
        print(f"Folder is empty")


if __name__ == '__main__':
    main()
