# !/usr/bin/env python3

"""
download_youtube_mp4_from_txt.py

Downloads YouTube videos in MP4 format from a list of URLs in a text file.

Description:
This module contains a function that reads a text file containing YouTube video URLs, fetches each video using the pytube library, and downloads it
in MP4 format to a specified folder.
"""

from download_youtube_mp4 import download_youtube


def main():
    folder = r"D:\YK\Downloads\Youtube"
    text_contains_link = r"D:\YK\Downloads\Youtube\Youtube Download Error URLS.txt"
    error_file = r"D:\YK\Downloads\Youtube\Youtube Download Error URLS2.txt"  # File to write URLs that caused exceptions

    with open(text_contains_link, "r") as file, open(error_file, "a") as error_file:
        links = file.readlines()
        for link in links:
            try:
                download_youtube(link.strip(), folder)
                print("\n")
            except Exception as e:
                print(f"Error downloading video: {e}")
                error_file.write(f"{link}")  # Write the URL to the file


if __name__ == '__main__':
    main()
