#!/usr/bin/env python3

"""
_add_photo_filter.py

This module is used for adding filters to photos.

Description:
This module contains functions that adjust the brightness of an image based on the average brightness of the image.
It reads images from an input folder, applies the brightness adjustment, and then saves the adjusted images to an output folder.
"""

# Script not working as expected

import os

import cv2
import numpy as np


def calculate_average_brightness(image):
    # Convert the image to the HSL color space
    hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # Calculate the average brightness (lightness)
    average_brightness = np.average(hsl_image[:, :, 1])

    return average_brightness


def adjust_brightness(image, brightness=75):
    # Convert the image to the HSL color space
    hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # Adjust the brightness (lightness)
    hsl_image[:, :, 1] = hsl_image[:, :, 1] * brightness / 100

    # Convert the image back to the BGR color space
    adjusted_image = cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)

    return adjusted_image


def main(_input_folder, _output_folder):
    # Check if output folder exists, if not, create it
    if not os.path.exists(_output_folder):
        os.makedirs(_output_folder)

    # Iterate over all images in the input folder
    for filename in os.listdir(_input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Load the image
            image = cv2.imread(os.path.join(_input_folder, filename))

            # Check if the image is loaded correctly
            if image is None:
                print(f"Failed to load image at {os.path.join(_input_folder, filename)}")
                continue

            # Calculate the average brightness of the image
            average_brightness = calculate_average_brightness(image)
            print(f"Average brightness before adjustment: {average_brightness}")

            # Adjust the brightness of the image
            adjusted_image = adjust_brightness(image, average_brightness + 70)

            # Calculate the average brightness of the adjusted image
            adjusted_brightness = calculate_average_brightness(adjusted_image)
            print(f"Average brightness after adjustment: {adjusted_brightness}")

            # Save the adjusted image to the output folder
            cv2.imwrite(os.path.join(_output_folder, filename), adjusted_image)


if __name__ == "__main__":
    input_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage\1 Image Source"
    output_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage\2 Image Toned"

    main(input_folder, output_folder)
