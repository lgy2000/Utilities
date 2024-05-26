#!/usr/bin/env python3

"""
get_video_info.py

This module is used to retrieve and display information about video files in a specified directory.

Description:
This module provides a function to iterate over all .mp4 files in a given directory, retrieve their dimensions, and print this information. It also
identifies and counts videos with dimensions below a certain threshold. The main function specifies the directory and calls the function to get
video information.
"""

import os

from moviepy.editor import VideoFileClip


def get_video_info(folder_path):
    n = 0
    m = 0
    low_dimension_video = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp4'):
            video = VideoFileClip(os.path.join(folder_path, file_name))
            print(f'{video.size[1]}\t{video.size[0]}\t\tVideo: {file_name}')
            if video.size[1] < 720 or video.size[0] < 1280:
                low_dimension_video.append(file_name)
                m += 1
            n += 1
    print(f'Total videos: {n}')
    print(f'Low dimension videos: {m}')


def main(_folder_path):
    get_video_info(_folder_path)


if __name__ == "__main__":
    folder_path = r"E:\All\7 Media\7.7 Fitness\Medium Quality\New folder - Copy"
    main(folder_path)
