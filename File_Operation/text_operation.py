class TextOperation:
    def __init__(self):
        # No need to initialize anything
        pass

    @staticmethod
    def clean_string(text):
        text = text.strip()  # Remove leading and trailing whitespace
        text = ' '.join(text.split())  # Remove extra spaces
        text = text.translate(str.maketrans('', '', '?!@$%^*:/\\=+{}<>'))  # Remove specific symbols
        return text

    def get_title_from_text(self, keyword, page_text):
        # Split the text using the title identifier
        title_parts = page_text.split(keyword) if keyword in page_text else page_text.split(keyword.upper())
        # Get the second part (the title itself)
        title = title_parts[1]
        # Clean the title
        title = self.clean_string(title)
        # If there are multiple lines in the title, combine them into one string
        title = " ".join(title.splitlines()[:3])[:60]
        return title
