# !/usr/bin/env python3

"""
download_youtube_mp4_from_txt.py

Downloads YouTube videos in MP4 format from a list of URLs in a text file.

Description:
This module contains a function that reads a text file containing YouTube video URLs, fetches each video using the pytube library, and downloads it
in MP4 format to a specified folder.
"""

from pytube import YouTube


def download_youtube(url, folder):
    yt = YouTube(url)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    print(yd)
    yd.download(folder)


def main():
    folder = r"D:\YK\Downloads\Youtube"
    text_contains_link = r"D:\YK\Downloads\youtube_links.txt"
    with open(text_contains_link, "r") as file:
        links = file.readlines()
        for link in links:
            download_youtube(link, folder)
            print("\n")


if __name__ == '__main__':
    main()
