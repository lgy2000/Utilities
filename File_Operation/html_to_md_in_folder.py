import os
import tkinter as tk
from tkinter import filedialog
from html2text import HTML2Text  # Correct import


def convert_html_to_md(html_content):
    """Convert HTML content to Markdown using html2text"""
    h = HTML2Text()  # Create instance directly from the class
    h.body_width = 0  # Disable line wrapping
    h.ignore_links = False  # Keep links by default
    return h.handle(html_content)


def process_files():
    # Create Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Ask user to select a directory
    selected_dir = filedialog.askdirectory(title="Select Folder with HTML Files")
    if not selected_dir:
        print("No folder selected. Exiting.")
        return

    # Create folder b
    output_dir = os.path.join(selected_dir, "b")
    os.makedirs(output_dir, exist_ok=True)

    # Process files
    for filename in os.listdir(selected_dir):
        if filename.lower().endswith('.html'):
            html_path = os.path.join(selected_dir, filename)
            md_filename = os.path.splitext(filename)[0] + '.md'
            md_path = os.path.join(output_dir, md_filename)

            try:
                # Read HTML file
                with open(html_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()

                # Convert to Markdown
                md_content = convert_html_to_md(html_content)

                # Write Markdown file
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)

                print(f"Converted: {filename} -> {md_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    print("\nConversion complete!")


if __name__ == "__main__":
    process_files()