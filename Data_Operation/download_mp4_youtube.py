# !/usr/bin/env python3

"""
download_mp4_youtube.py

Downloads a YouTube video in MP4 format.

Description:
This module contains a function that takes a YouTube video URL as input, fetches the video using the pytube library, and downloads it in MP4 format
to a specified folder.
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
    link = input("Youtube Video link: ")
    while link:
        download_youtube(link, folder)
        print("\n")
        link = input("Youtube Video link: ")


if __name__ == '__main__':
    main()
