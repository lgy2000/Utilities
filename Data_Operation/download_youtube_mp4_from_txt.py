# !/usr/bin/env python3

"""
download_youtube_mp4_from_txt.py

Downloads YouTube videos in MP4 format from a list of URLs in a text file.

Description:
This module contains a function that reads a text file containing YouTube video URLs, fetches each video using the pytube library, and downloads it
in MP4 format to a specified folder.
"""

from pytube.__main__ import YouTubeHack


def download_youtube(url, folder):
    yt = YouTubeHack(url)  # Use OAuth to avoid the 403 error (HTTP Error 403: Forbidden
    print("URL: ", url)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    print(yd)
    yd.download(folder)


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
