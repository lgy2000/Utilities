import os
import zipfile

from lxml import etree

# Define the folder path containing the EPUB files.
bookpath = r"D:\YK\Downloads\Book"
book_list = []


def get_epub_info(fname):
    """
    Extracts metadata from an EPUB file.

    Parameters:
    fname (str): The file path of the EPUB file.

    Returns:
    dict: A dictionary containing the title, author, publication year, and ISBN of the EPUB.
    """
    # Define the namespaces used in the EPUB metadata.
    ns = {
        'n': 'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg': 'http://www.idpf.org/2007/opf',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }

    try:
        with zipfile.ZipFile(fname, 'r') as zip:
            # Find the contents metafile.
            txt = zip.read('META-INF/container.xml')
            tree = etree.fromstring(txt)
            cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path', namespaces=ns)[0]

            # Grab the metadata block from the contents metafile.
            cf = zip.read(cfname)
            tree = etree.fromstring(cf)
            p = tree.xpath('/pkg:package/pkg:metadata', namespaces=ns)[0]

            # Extract metadata.
            res = {}
            res['title'] = p.xpath('dc:title/text()', namespaces=ns)[0] if p.xpath('dc:title/text()', namespaces=ns) else 'Unknown Title'
            res['author'] = p.xpath('dc:creator/text()', namespaces=ns)[0] if p.xpath('dc:creator/text()', namespaces=ns) else 'Unknown Author'
            # Extract the year from the date, or set as 'Unknown Year' if not available.
            date = p.xpath('dc:date/text()', namespaces=ns)
            res['pub_year'] = date[0][:4] if date else 'Unknown Year'
            # Extract the ISBN by checking all identifier elements.
            res['isbn'] = 'Unknown ISBN'
            identifiers = p.xpath('dc:identifier', namespaces=ns)
            for identifier in identifiers:
                id_text = identifier.text
                if id_text and ('isbn' in id_text.lower() or 'urn' in id_text.lower()):
                    res['isbn'] = id_text
                    break

            return res

    except zipfile.BadZipFile:
        # Handle the case where the file is not a valid zip file.
        print(f"Error: File {fname} is not a zip file or is corrupted.")
        return None
    except Exception as e:
        # Handle any other exceptions.
        print(f"Error processing file {fname}: {e}")
        return None


def prompt_for_year(title, author):
    """
    Prompts the user to input a year for a book with an unknown year.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.

    Returns:
    str: The publication year entered by the user.
    """
    while True:
        try:
            year = input(f"Enter the publication year for '{author} - {title}': ")
            if year.isdigit() and len(year) == 4:
                return year
            else:
                print("Invalid year format. Please enter a 4-digit year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")


# Iterate through each file in the specified directory.
for book in os.listdir(bookpath):
    book_path = os.path.join(bookpath, book)
    # Check if the file is an EPUB.
    if os.path.isfile(book_path) and book_path.lower().endswith('.epub'):
        info = get_epub_info(book_path)
        if info:
            title = info['title']
            author = info['author']
            pub_year = info['pub_year']
            isbn = info['isbn']
            # Print the extracted metadata.
            print(f"Title: {title}, Author: {author}, \nYear: {pub_year}, ISBN: {isbn}")

            # Replace invalid characters in the title.
            safe_title = title.replace(":", " -").replace("?", "").replace("\"", "").replace("/", "x").replace("'", "").title()

            # If publication year is unknown, prompt the user.
            if pub_year == 'Unknown Year':
                pub_year = prompt_for_year(title, author)

            # Create a new file name
            new_title = f"{author} - {safe_title} ({pub_year}).epub"
            new_path = os.path.join(bookpath, new_title)
            book_list.append(new_title)
            try:
                # Rename the file to the new title.
                os.rename(book_path, new_path)
                print(f"Renamed {book_path} \nto {new_path}\n")
            except Exception as e:
                # Handle any exceptions that occur during renaming.
                print(f"Error renaming file {book_path} \nto {new_path}: {e}\n")

for book in book_list:
    print(book)
