import imaplib
import email

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


# Function to decode email header
def decode_header(header):
    decoded_header = email.header.decode_header(header)
    decoded_str = []
    for decoded_part, encoding in decoded_header:
        if isinstance(decoded_part, bytes):
            decoded_str.append(decoded_part.decode(encoding or 'utf-8'))
        elif isinstance(decoded_part, str):
            decoded_str.append(decoded_part)
    return ''.join(decoded_str)
