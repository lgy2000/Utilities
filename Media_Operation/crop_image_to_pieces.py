#!/usr/bin/env python3

"""
crop_image_to_pieces.py

This module is used for cropping an image into multiple pieces.

Description:
This module contains functions that take an image as input, crop it into a square, and then split it into multiple smaller square pieces. It also
includes a function to convert jpg images to png.
"""

import os

import cv2
from PIL import Image


def convert_jpg_to_png(jpg_path, png_path):
    # Open the image file
    img = Image.open(jpg_path)
    # Save as PNG
    img.save(png_path, "PNG")


def is_square(image):
    return image.shape[0] == image.shape[1]


def crop_to_square(image):
    print("Cropping the image to a square")
    size = min(image.shape[0], image.shape[1])
    start_row = (image.shape[0] - size) // 2
    start_col = (image.shape[1] - size) // 2
    return image[start_row:start_row + size, start_col:start_col + size]


def split_image(image, pieces):
    print(f"Splitting the image into pieces of {pieces}x{pieces}")
    size = image.shape[0] // pieces
    return [image[i * size:(i + 1) * size, j * size:(j + 1) * size] for i in range(pieces) for j in range(pieces)]


def process_image(image_path, output_folder, pieces=3):
    print(f"Processing the image: {image_path}")
    image = cv2.imread(image_path)
    if not is_square(image):
        image = crop_to_square(image)
    split_images = split_image(image, pieces)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    original_filename = os.path.splitext(os.path.basename(image_path))[0]
    for i, img in enumerate(split_images):
        i += 1
        cv2.imwrite(os.path.join(output_folder, f"{original_filename}-{i}.png"), img)
        print(f"Saved {original_filename}-{i}.png")


def main(input_folder, output_folder, pieces=3):
    print(f"Processing all images in the folder: {input_folder}")
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            png_filename = filename.replace(".jpg", ".png")
            convert_jpg_to_png(os.path.join(input_folder, filename), os.path.join(input_folder, png_filename))
            process_image(os.path.join(input_folder, png_filename), output_folder, pieces)
            print("\n")
        elif filename.endswith(".png"):
            process_image(os.path.join(input_folder, filename), output_folder, pieces)
            print("\n")


if __name__ == "__main__":
    input_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage\2 Image Toned"
    output_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage\3 Image Cut (Post in Descending Cut Order)"
    pieces = 3
    main(input_folder, output_folder, pieces)
