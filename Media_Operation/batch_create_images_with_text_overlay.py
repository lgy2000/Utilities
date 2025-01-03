#!/usr/bin/env python3

"""
batch_create_images_with_text_overlay.py

This module is used for creating images with text overlays in batch.

Description:
This module contains a function that takes a list of images and a list of texts as input. It overlays each text on the corresponding image and
saves the result. The text overlay can be customized with various parameters such as font, size, color, and position.
"""

import datetime
import os

import cv2
import pandas as pd

def get_date_today():
    # Get today's date
    today = datetime.date.today()
    # Format the date as a string
    date_str = today.strftime('%Y.%m.%d')
    return date_str


def batch_create_images_with_text_overlay(excel_file, image_folder, output_folder, font, font_scale, font_thickness, max_text_width_ratio,
                                          line_spacing):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():

        # Check if 'Generated Post?' is 0
        if df.loc[index, 'Generated Post?'] == 0:

            # Get the text, image filename, and schedule
            text = row['Content 1']
            image_filename = row['Image Filename 1']
            schedule = row['Schedule 1']

            # Open the image
            img = cv2.imread(os.path.join(image_folder, image_filename))

            # Check if the image is loaded correctly
            if img is None:
                print(f"Failed to load image: {image_filename}")

                # Update the "Generated Post?" column in the DataFrame
                df.loc[index, 'Generated Post?'] = 0

                continue

            # Calculate the maximum width for the text
            max_text_width = int(img.shape[1] * max_text_width_ratio)  # 80% of the image width

            # Split the text into lines
            words = text.split(' ')
            lines = []
            line = ''
            for word in words:
                if cv2.getTextSize(line + ' ' + word, font, font_scale, font_thickness)[0][0] > max_text_width:
                    lines.append(line)
                    line = word
                else:
                    line += ' ' + word
            lines.append(line)

            # Calculate the total height of the text
            total_text_height = sum([cv2.getTextSize(line, font, font_scale, font_thickness)[0][1] for line in lines]) + 22 * (
                    len(lines) - 1)  # Increase line spacing

            # Calculate the starting y-coordinate for the text
            y = (img.shape[0] - total_text_height) // 2

            # Draw each line on the image
            for line in lines:
                # Get the width and height of the text box
                text_size, _ = cv2.getTextSize(line, font, font_scale, font_thickness)

                # Calculate the x-coordinate for the center of the image
                x = (img.shape[1] - text_size[0]) // 2

                # Draw the text on the image
                cv2.putText(img, line.strip(), (x, y), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

                # Update the y-coordinate for the next line
                y += text_size[1] + line_spacing  # Increase line spacing or line height

            # Save the image to the output folder with the original name prefixed with schedule
            image_filename, extension = os.path.splitext(image_filename)
            output_filename = f"{image_filename} {schedule}{extension}"
            output_filename = output_filename.replace(' 00:00:00', '')  # Replace colons with underscores
            cv2.imwrite(os.path.join(output_folder, output_filename), img)

            print(f"Saved image: {output_filename}")

            # Update the "Generated Post?" column in the DataFrame
            df.loc[index, 'Generated Post?'] = 1
        else:
            # Remove the row from the DataFrame
            df = df.drop(index)

    # Write the updated DataFrame back to the Excel file
    date = get_date_today()
    excel_folder, excel_filename = os.path.split(excel_file)
    excel_filename, extension = os.path.splitext(excel_filename)
    excel_file2 = f"{excel_folder}\\{excel_filename} ({date} Generated){extension}"
    df.to_excel(excel_file2, index=False)


def main(_excel_file, _image_folder, _output_folder, _font, _font_scale, _font_thickness, _max_text_width_ratio, _line_spacing):
    batch_create_images_with_text_overlay(_excel_file, _image_folder, _output_folder, _font, _font_scale, _font_thickness, _max_text_width_ratio,
                                          _line_spacing)
    os.startfile(_output_folder)


if __name__ == "__main__":
    excel_file = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage - Copy\Content & Schedule.xlsx"
    image_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage - Copy\3 Image Cut (Post in Descending Cut Order)"
    output_folder = r"D:\YK\Resources\.5 Work\2024 Instagram\1 Self-Affirmations - positivitysage - Copy\4 Image Post"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.65
    font_thickness = 4
    max_text_width_ratio = 0.82
    line_spacing = 34

    main(excel_file, image_folder, output_folder, font, font_scale, font_thickness, max_text_width_ratio, line_spacing)
