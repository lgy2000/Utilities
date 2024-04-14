def compress_pdf():
    writer = PdfWriter(clone_from="example.pdf")
    for page in writer.pages:
        page.compress_content_streams()  # This is CPU intensive!
    with open("out.pdf", "wb") as f:
        writer.write(f)
