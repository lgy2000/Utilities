#!/usr/bin/env python3

"""
_add_title_overlay_moviepy.py

Adds a title overlay to a video using MoviePy.

Description:
This module provides a function to add a title overlay to the first frame of a video. It uses the MoviePy library to load the video,
cut it into subclips, concatenate the subclips, add the title overlay, and save the final clip to a file. It also handles exceptions and logs any
errors that occur during this process.
Suggest to use Adobe Premiere Pro with Automation Block for editing and exporting higher quality video, and maybe Adobe Media Encoder for faster
media exporting and conversion.
"""

# Script not working as expected

import gc
import os
import sys
import traceback
from tkinter import filedialog

import moviepy.editor as mpy
from eglogging import logging_load_human_config, CRITICAL

logging_load_human_config()


def add_title_overlay(loadtitle, savetitle, title, video_codec, compression):
    # Load video file
    video = mpy.VideoFileClip(loadtitle)

    # Add text to the clip
    txt = mpy.TextClip(txt=title, font='Courier', fontsize=24, color='black', bg_color='WhiteSmoke', method='caption', align="North")
    txt = txt.set_start(0)  # (min, s)
    txt = txt.set_duration(5)
    # txt = txt.crossfadein(0)
    # txt = txt.crossfadeout(0.5)
    # txt = txt.set_position((0.05, 0.05), relative=True)

    # Add text to final clip
    final_clip = mpy.CompositeVideoClip([video, txt])

    # Save final clip to file
    final_clip.write_videofile(savetitle, threads=6,
                               codec=video_codec,
                               preset=compression,
                               ffmpeg_params=["-crf", "22"])

    # Close video file
    video.close()


def main(_video_codec, _compression):
    try:
        # folder = filedialog.askdirectory()
        # file_ops = FileOperation()
        # _, folder = file_ops.copy_folder_and_files(folder)

        file1 = filedialog.askopenfilename()
        folder_path, filename1 = os.path.split(file1)
        filename, extension = os.path.splitext(filename1)
        filename2 = f"{filename} (2){extension}"
        file2 = os.path.join(folder_path, filename2)

        add_title_overlay(file1, file2, filename, _video_codec, _compression)

        # Call gc.collect() to free up memory immediately
        gc.collect()
    except Exception as ex:
        CRITICAL("Exception: {}".format(ex))
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    # Define video codec and quality
    video_codec = "mpeg4"
    compression = "faster"

    main(video_codec, compression)
