# !/usr/bin/env python3

"""
kindle_operation.py

Handles the conversion of Kindle notes from HTML to Markdown format.

Description:
This module defines the KindleOperation class, which provides methods for parsing an HTML file of Kindle notes,
converting the notes to Markdown format, and exporting the output to a file or the clipboard. It also handles
various options such as whether to include the location of notes/highlights and whether to override an existing output file.
"""

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
        Retrieves the most recently added note in the current chapter.
        Returns:
            Notes: The most recently added note object.
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
        Parses the given HTML file and extracts the notes.
        Args:
            html_file (str): The path to the HTML file to be parsed.
        """
        soup = self._read_parse_file(html_file)
        all_divs = self._get_all_divs(soup)
        self._process_divs(all_divs)

    @staticmethod
    def _read_parse_file(html_file):
        """
        Reads the contents of the given HTML file and parses it using BeautifulSoup.
        Args:
            html_file (str): The path to the HTML file to be read and parsed.
        Returns:
            BeautifulSoup: The parsed HTML content.
        """
        with open(html_file, 'r', encoding='utf8') as fp:
            htmls = fp.read()
        soup = BeautifulSoup(htmls, 'html.parser')
        return soup

    @staticmethod
    def _get_all_divs(soup):
        """
        Retrieves all div elements from the given BeautifulSoup object.
        Args:
            soup (BeautifulSoup): The parsed HTML content.
        Returns:
            list: A list of all div elements in the parsed HTML content.
        """
        all_divs = soup.select('[class]')
        return all_divs

    def _process_divs(self, all_divs):
        """
        Processes div elements from an HTML file, extracting notes.
        It iterates through each div, capturing its class attribute and text content. Depending on the class, it identifies and handles book
        titles, authors, section headings, note headings, and note text.
        Args:
            all_divs (list): A list of all div elements in the parsed HTML content.
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
        Processes a div element representing a note heading.
        It extracts the note's source, location (given by Kindle), and type (either 'Note' or 'Highlight'). If the last note type was 'Note',
        it attempts to retrieve the last note added to the current chapter; otherwise, it initializes a new `Notes` object and adds it to the
        chapter's notes.
        Args:
            div (bs4.element.Tag): The div element to be processed.
        Returns:
            tuple: A tuple containing the source, location, last note type, and work-in-progress (WIP) note.
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
        Processes a div element as note text, extracting the note's text and assigning it to the appropriate attribute of the Notes object based on
        the note type ('Highlight' or 'Note'). If the last note type was 'Highlight,' the text is assigned to the text attribute; if it was 'Note,
        ' the text is assigned to the note attribute.
        Args:
            div_contents (str): The text content of the div element.
            last_note_type (str): The type of the last note.
            wip_note (Notes): The work-in-progress note.
        Returns:
            tuple: A tuple containing the last note type and the work-in-progress note.
        """
        div_contents = div_contents.split('\n')[0]
        if last_note_type == 'Highlight':
            wip_note.text = div_contents
        elif last_note_type == 'Note':
            wip_note.note = div_contents
        return last_note_type, wip_note

    def output_md(self, args):
        """
        Main entry point of the script. It parses the command line arguments, reads the input HTML file,
        converts it to Markdown format, and writes the output to a file or clipboard based on the arguments.
        Returns:
            None
        """
        md = self._create_md_header()
        md += self._create_md_body(args)
        self._output_markdown_to_destination(md, args)

    def _create_md_header(self):
        """
        Creates the header for the Markdown document, which includes the book title and the author.
        Returns:
            str: The Markdown-formatted header.
        """
        # Format the book title and author into a Markdown header
        md = "\n\n# {}\n".format(self.book_title)
        md += "- {}\n".format(self.author)
        return md

    def _create_md_body(self, args):
        """
        Creates the body for the Markdown document by iterating over all chapters and notes,
        and formatting them into a Markdown document.
        Args:
            args (argparse.Namespace): The parsed command line arguments.
        Returns:
            str: The Markdown-formatted body.
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
    def _output_markdown_to_destination(md, args):
        """
        Outputs the given Markdown string to the appropriate location, either to the clipboard or a file.
        Args:
            md (str): The Markdown-formatted string.
            args (argparse.Namespace): The parsed command line arguments.
        Returns:
            None
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
                INFO("The Markdown file has already exists. Use -y or --override flag.", LOG_COLORS['RED'])
        # print(args)

    # TODO: Implement the following methods

    def _get_book_info(self):
        """
        Get the book title and author from the parsed HTML.
        """
        # This is a placeholder. The actual implementation will depend on the structure of your HTML file.
        # Might extract book info from the HTML file or get from the internet
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
