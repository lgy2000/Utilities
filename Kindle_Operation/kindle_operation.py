"""
kindle_operation.py

Provides functionality to convert an HTML file of book notes exported from an Amazon Kindle to a Markdown document.

Description:
This module contains the KindleOperation class which has methods to parse the HTML file, extract notes, and output them in a Markdown format. It also
includes the Note and Chapter_notes classes to structure the notes data.
"""

# !/usr/bin/env python3
import os
from collections import OrderedDict

import pyperclip
from bs4 import BeautifulSoup
from eglogging import logging_load_human_config, INFO, LOG_COLORS

# Configure logging
logging_load_human_config()


# -nl, --no-location    -Do not include the source location of each note/highlight
# -c, --clipboard       -Export .md directly to the clipboard instead of file
# -y, --override        -Override .md file if one already exists
# -o OUTPUT, --output   -A file to which save the Markdown document


class Notes:
    """
    This class represents a highlight, possibly including a note, from the Kindle book.
    Attributes:
        text (str): The book text that was highlighted.
        note (str): Any note added.
        source (str): Info about the source of this note (location etc.).
        location (int): Location as given by Kindle.
    """

    def __init__(self):
        """
        Initialize a new instance of the Note class.
        """
        self.text = ''  # the book text that was highlighted
        self.note = ''  # any note added
        self.source = ''  # info about the source of this note (location etc.)
        self.location = None  # int Location as given by Kindle


class ChapterNotes:
    """
    This class represents the notes for a specific chapter in the Kindle book.
    Attributes:
        title (str): Name of this chapter.
        notes (OrderedDict): Location (int) -> [Note]"""

    def __init__(self, chapter_title=''):
        """
        Initialize a new instance of the Chapter_notes class.
        """
        self.title = chapter_title  # name of this chapter
        self.notes = OrderedDict()  # Location (int) -> [Note]

    def get_last_note(self):
        """
        Returns the most recently-added note.
        """
        return self.notes[next(reversed(self.notes))]


class KindleOperation:
    """
    This class represents the notes for a Kindle book.
    Attributes:
        book_title (str): Title of the book.
        author (str): Author of the book.
        chapter_notes (list): List of Chapter_notes.
    """

    def __init__(self):
        """
        Initialize a new instance of the KindleOperation class.
        """
        self.book_title = ''
        self.author = ''
        self.chapter_notes = []  # list of Chapter_notes

    def parse_file(self, html_file):
        """
        Parse the given HTML file and extract the notes.
        """
        soup = self._read_parse_file(html_file)
        all_divs = self._get_all_divs(soup)
        self._process_divs(all_divs)

    @staticmethod
    def _read_parse_file(html_file):
        """
        Read the contents of the given HTML file and parse the given HTML string using BeautifulSoup.
        """
        with open(html_file, 'r', encoding='utf8') as fp:
            htmls = fp.read()
        soup = BeautifulSoup(htmls, 'html.parser')
        return soup

    @staticmethod
    def _get_all_divs(soup):
        """
        Get all div elements from the given BeautifulSoup object.
        """
        all_divs = soup.select('[class]')
        return all_divs

    def _process_divs(self, all_divs):
        """
        Process the given div elements and extract the notes.
        This method iterates over all div elements in the parsed HTML file. For each div, it gets the class attribute and the text content.
        Depending on the class attribute, it processes the div as a book title, author, section heading, note heading, or note text.
        """
        # Initialize variables for the work-in-progress note and the last note type
        wip_note = None
        last_note_type = ''

        # Iterate over all div elements
        for div in all_divs:
            # Get the class attribute of the div
            c = div['class'][0]

            try:
                # Get the text content of the div, stripping any leading/trailing whitespace and replacing multiple spaces with a single space
                div_contents = div.get_text().strip().replace('  ', ' ').replace(u' \xa0', '')
            except AttributeError as e:
                div_contents = None
                print(f"Error: {e}")

            # Process the div based on its class attribute
            if c == 'bookTitle':
                self.book_title = div_contents
            elif c == 'authors':
                self.author = div_contents
            elif c == 'sectionHeading':
                self.chapter_notes.append(ChapterNotes(div_contents))
            elif c == 'noteHeading':
                _, _, last_note_type, wip_note = self._process_note_heading(div)
            elif c == 'noteText':
                last_note_type, wip_note = self._process_note_text(div_contents, last_note_type, wip_note)

    def _process_note_heading(self, div):
        """
        Process the given div element as a note heading.
        This method processes a div element that represents a note heading. It extracts the source and location of the note from the div element.
        The source is a string that contains information about the source of the note, and the location is an integer that represents the location
        of the note as given by Kindle.
        The method also determines the type of the note (whether it's a 'Note' or 'Highlight') and initializes a new `Notes` object if necessary.
        If the last note type was 'Note', it tries to get the last note added to the current chapter. If it can't find one, it initializes a new
        `Notes` object and adds it to the current chapter's notes.
        """
        # Extract the source and location of the note from the div element
        source = ' '.join(div.stripped_strings)
        location = int(source.split()[-1])

        # Determine the type of the note
        last_note_type = source.split()[0]

        # If the last note type was 'Note', try to get the last note added to the current chapter
        if last_note_type == 'Note':
            try:
                wip_note = self.chapter_notes[-1].get_last_note()
            except Exception as e:
                wip_note = None
                print(f"Error: {e}")
        else:
            wip_note = None

        # If no work-in-progress note was found, initialize a new `Notes` object and add it to the current chapter's notes
        if wip_note is None:
            wip_note = Notes()
            wip_note.location = location
            wip_note.source = ' '.join(div.stripped_strings)
            self.chapter_notes[-1].notes[location] = wip_note

        return source, location, last_note_type, wip_note

    @staticmethod
    def _process_note_text(div_contents, last_note_type, wip_note):
        """
        Process the given div element as a note text.
        This method processes a div element that represents a note text. It extracts the text of the note from the div element and assigns it to
        the appropriate attribute of the `Notes` object depending on the type of the note. If the last note type was 'Highlight', it assigns the
        text to the `text` attribute of the `Notes` object. If the last note type was 'Note', it assigns the text to the `note` attribute of the
        `Notes` object.
        """
        div_contents = div_contents.split('\n')[0]
        if last_note_type == 'Highlight':
            wip_note.text = div_contents
        elif last_note_type == 'Note':
            wip_note.note = div_contents
        return last_note_type, wip_note

    def output_md(self, args):
        """
        Create the header for the Markdown document.
        This method creates the header for the Markdown document. The header includes the book title and the author.
        """
        md = self._create_md_header()
        md += self._create_md_body(args)
        self._output_md(md, args)

    def _create_md_header(self):
        """
        Create the header for the Markdown document.
        This method creates the header for the Markdown document. The header includes the book title and the author.
        """
        # Format the book title and author into a Markdown header
        md = "\n\n# {}\n".format(self.book_title)
        md += "- {}\n".format(self.author)
        return md

    def _create_md_body(self, args):
        """
        Create the body for the Markdown document.
        This method iterates over all chapters and notes, formatting them into a Markdown document. It also includes the source of each note if the
        'location' argument is True.
        """
        # Initialize an empty string for the Markdown body
        md = ""
        # Iterate over all chapters
        for chapter in self.chapter_notes:
            # Add the chapter title to the Markdown body
            md += "## {}\n".format(chapter.title)
            # Iterate over all notes in the chapter
            for location in chapter.notes:
                note = chapter.notes[location]
                # Add the note text to the Markdown body
                md += "- {}\n".format(note.text)
                # If the note has a note text, add it to the Markdown body
                if note.note != '':
                    md += "    - **{}**\n".format(note.note)
                # If the 'location' argument is True, add the note source to the Markdown body
                if args.location:
                    md += "    - {}\n".format(note.source)
            md += "\n"
        return md

    @staticmethod
    def _output_md(md, args):
        """
        Output the given Markdown string to the appropriate location.
        This method outputs the given Markdown string to the clipboard if the 'clipboard' argument is True. Otherwise, it writes the Markdown
        string to a file. If the file already exists and the 'override' argument is False, it prints an error message.
        """
        print("\n")

        # If the 'clipboard' argument is True, copy the Markdown string to the clipboard
        if args.clipboard:
            pyperclip.copy(md)
            INFO("Copied the output to clipboard", LOG_COLORS['GREEN'])
        else:
            # If the 'output' argument is not provided, set the output file to the same location as the input file with a .md extension
            if not args.output:
                args.output = os.path.splitext(args.input)[0] + '.md'
            # If the output file doesn't exist or the 'override' argument is True, write the Markdown string to the file
            if not os.path.exists(args.output) or args.override:
                with open(args.output, 'w', encoding='utf8') as fp:
                    fp.write(md)
                INFO("Output to {}".format(args.output), LOG_COLORS['GREEN'])
            else:
                # If the output file exists and the 'override' argument is False, print an error message
                INFO("Could not save .md file, because it already exists. Use --override flag.", LOG_COLORS['RED'])
        print(args)

    # ================================================================================================================
    # TO-DO LIST
    # ================================================================================================================
    def _get_book_info(self):
        """
        Get the book title and author from the parsed HTML.
        """
        # This is a placeholder. The actual implementation will depend on the structure of your HTML file.
        pass

    def _extract_notes_only(self, soup):
        """
        Extract notes from the parsed HTML.
        """
        # This is a placeholder. The actual implementation will depend on the structure of your HTML file.
        pass

    def _extract_highlights_only(self, soup):
        """
        Extract notes from the parsed HTML.
        """
        # This is a placeholder. The actual implementation will depend on the structure of your HTML file.
        pass

    def _format_notes(self):
        """
        Format the extracted notes for output.
        """
        # This is a placeholder. The actual implementation will depend on how you want to format your notes.
        pass
