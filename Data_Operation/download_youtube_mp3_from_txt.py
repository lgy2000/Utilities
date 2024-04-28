# !/usr/bin/env python3

"""
download_youtube_mp3_from_txt.py

Downloads YouTube videos and converts them to MP3 format from a list of URLs in a text file.

Description:
This module contains a function that reads a text file containing YouTube video URLs, fetches each video using the pytube library, downloads it
in MP4 format to a specified folder, and then converts the downloaded video to MP3 format using the moviepy library.
"""

from moviepy.editor import AudioFileClip
from pytube import YouTube


def download_youtube(url, folder):
    yt = YouTube(url)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    print(yd)
    output_path = yd.download(folder)

    # Convert the downloaded video to mp3
    clip = AudioFileClip(output_path)
    clip.write_audiofile(output_path.replace(".mp4", ".mp3"))


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
