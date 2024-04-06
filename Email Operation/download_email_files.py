"""
download_email_files.py

Description:
Download all files in an email folder

Notes:
- Input values for the configuration variables in config.py.
"""

import os
import quopri

from config import email_folder, input_folder, require_original_filename
from get_email import login_email, decode_header
from credentials import email_address, password

# Function to save attachment
def save_attachment(part, filename):
    save_path = os.path.join(input_folder, filename)
    with open(save_path, "wb") as f:
        f.write(part.get_payload(decode=True))
        print(f"Attachment '{filename}' saved successfully.")
    return save_path


# Function to rename file
def rename_file(filename, subject, require_ori_filename):
    file_root, file_ext = os.path.splitext(filename)
    new_filename = f"{subject} {' ' + file_root if require_ori_filename else ''}{file_ext}"
    return new_filename


# Main function to download and process emails
def process_attachments():
    mail, result, data = login_email(email_address, password, email_folder)

    if result == "OK":
        for num in data[0].split():
            result, data = mail.fetch(num, "(RFC822)")
            if result == "OK":
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                subject = decode_header(msg["Subject"])
                print(f"Processing email with subject: {subject}")

                # Counter for multiple attachments with the same subject
                subject_counter = 1

                # Iterate over email parts
                for part in msg.walk():
                    if part.get_content_maintype() == "multipart":
                        continue
                    if part.get("Content-Disposition") is None:
                        continue

                    # Download attachment
                    filename = decode_header(part.get_filename())
                    filename = quopri.decodestring(filename).decode('utf-8')  # Decode Quoted-Printable encoding
                    filename = os.path.basename(filename)  # Ensure proper filename extraction
                    if filename:
                        save_path = save_attachment(part, filename)

                        # Rename the file
                        new_filename = rename_file(filename, subject, require_original_filename)

                        # Check if the new filename already exists in the save directory
                        while os.path.isfile(os.path.join(input_folder, new_filename)):
                            # Append a unique identifier to the filename
                            subject_counter += 1
                            new_filename = f"{subject} {' ' + os.path.splitext(filename)[0]} ({subject_counter}){os.path.splitext(filename)[1]}"

                        # Rename the file to the new filename
                        os.rename(save_path, os.path.join(input_folder, new_filename))
                        print(f"Renamed file to '{new_filename}'")
    else:
        print("Failed to search emails.")

    # Logout and close connection
    mail.logout()


def main():
    process_attachments()
    print(f"Finish downloading emails in folder: {email_folder}")


if __name__ == '__main__':
    main()
