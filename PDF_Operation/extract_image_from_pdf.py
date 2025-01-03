import fitz
import io
from PIL import Image
import os


def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Iterate over each page
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base = img[1]
            img_data = doc.extract_image(xref)
            img_bytes = img_data['image']

            # Convert bytes to image
            image = Image.open(io.BytesIO(img_bytes))

            # Save each image to a file
            image.save(os.path.join(output_folder, f"{base}.png"))


if __name__ == "__main__":
    pdf_path = r"D:\YK\Downloads\Doc1.pdf"
    output_folder = r"D:\YK\Downloads\New folder"  # replace with your output folder path
    extract_images_from_pdf(pdf_path, output_folder)
