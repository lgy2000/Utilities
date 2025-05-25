"""
download_pdf_from_website.py

This module is used to download PDF or MP3 files from a website.

Description:
This module contains functions to extract all media links from a website, validate these links, and download the media files. It uses BeautifulSoup
to parse the website and requests to download the files.
"""

import os
import re
import urllib.parse
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def get_all_main_page_links(base_url, start_page, end_page):
    urls = []
    for page in range(start_page, end_page + 1):
        url = f"{base_url}?page={page}"
        urls.append(url)
    return urls


def is_page_valid(url, base_url):
    # Remove 'https://www.' and 'https://' from the URLs
    url = url.replace("https://www.", "").replace("https://", "")
    base_url = base_url.replace("https://www.", "").replace("https://", "")
    # Parse the URLs
    parsed = urlparse(url)
    parsed_base = urlparse(base_url)
    # Check if the netloc of both URLs are the same and if the base URL is in the URL
    return parsed.netloc == parsed_base.netloc and base_url in url


# Function to get all links from a webpage
def get_all_page_links(session, url, headers, domain_url):
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    scripts = soup.find_all('script')
    page_links = []

    for script in scripts:
        # Check if the script tag has content
        if script.string:
            # Find all matches of the pattern "pn\" in the script string
            matches = re.findall(r'"([^"]*pn[^"]*)"', script.string)
            for match in matches:
                # Decode the URL before appending
                decoded_url = urllib.parse.unquote(match.replace('\\u002F', '/'))
                # Join the 'decoded_url' with the domain URL
                full_url = urljoin(domain_url, decoded_url)
                # Check if 'full_url' contains "cms" and "/pn"
                if "cms" in full_url and "/pn" in full_url:
                    # Add 'full_url' to the links list
                    page_links.append(full_url)

    # Return the list of links
    return page_links


def get_all_media_links(session, url, headers):
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    scripts = soup.find_all('script')
    media_links = []

    for script in scripts:
        if script.string:  # Check if the script tag has content
            matches = re.findall(r'"([^"]*assets[^"]*(pdf|mp3)[^"]*)"', script.string)
            for match in matches:
                # Decode the URL before appending
                decoded_url = urllib.parse.unquote(match[0].replace('\\u002F', '/'))
                media_links.append(decoded_url)

    return media_links


# Function to read a file, returns the content of the file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def is_media_link_valid(media_link, existing_links):
    if not (media_link.endswith(".mp3") or media_link.endswith(".pdf")):
        return False
    media_link_last_part = media_link.split('/')[-1].replace("-", " ")
    print(f"Media Link Last Part: {media_link_last_part}")
    if media_link_last_part.lower() in existing_links.lower():
        return False
    return True


# Function to download a file from a URL
def download_file(url, pathname, headers):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    # Get the file title from the URL
    file_title = os.path.splitext(os.path.basename(url))[0]
    # Convert the file title to title case and replace '-' and '_' symbols with spaces
    file_title = file_title.title().replace('-', ' ').replace('_', ' ')
    # Form the filename
    filename = f"{file_title}.pdf" if url.endswith(".pdf") else f"{file_title}.mp3"
    # Create the directory if it doesn't exist
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # Form the path of the file
    file_path = os.path.join(pathname, filename)
    # Download the file
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded file: {file_path}")


# Main function
def main(email_address_heroic, email_password_heroic):
    domain_url = r"https://www.heroic.us"
    base_url = r"https://www.heroic.us/pn"
    download_path = r"D:\YK\Downloads\heroic"

    start_page = 20
    end_page = 30

    # html_path = r"D:\YK\Downloads\html.txt"
    # html_script = read_file(html_path)

    existing_links_file_path = r"D:\YK\Python\Utilities\Data_Operation\Existing Links.txt"
    existing_links = read_file(existing_links_file_path)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # URL for the login page
    login_url = 'https://www.heroic.us/account/sign-in?returnUrl=%2Fdashboard'
    # Your login credentials
    payload = {
        'username': email_address_heroic,
        'password': email_password_heroic
    }
    # Start a session
    with requests.Session() as session:
        # Send a POST request to the login URL with your credentials
        session.post(login_url, data=payload, headers=headers)

        # Now you are logged in and can make requests as a logged-in user
        session.get(domain_url, headers=headers)

        main_page_links = get_all_main_page_links(base_url, start_page, end_page)
        for main_page_link in main_page_links:
            print(f"\n\nProcessing Main Page: {main_page_link}")
            for page_link in get_all_page_links(session, main_page_link, headers, domain_url):
                # Check if the link is valid
                if is_page_valid(page_link, base_url):
                    print(f"\nProcessing Page: {page_link}")
                    # Loop through all links from the link
                    for media_link in get_all_media_links(session, page_link, headers):
                        print(f"Content: {media_link}")
                        # Check if the file link ends with '.pdf' or '.mp3'
                        if is_media_link_valid(media_link, existing_links):
                            # Download the file
                            download_file(media_link, download_path, headers)
        else:
            print(f"Skipping {main_page_link} due to failed HTML script retrieval.")


# Run the main function
if __name__ == "__main__":
    from config import email_address_heroic, email_password_heroic
    main(email_address_heroic, email_password_heroic)
