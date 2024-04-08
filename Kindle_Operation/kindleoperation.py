"""
kindle_operation.py

Provides functionality to convert an HTML file of book notes exported from an Amazon Kindle to a Markdown document.

Description:
This module contains the Kindle_notes class which has methods to parse the HTML file, extract notes, and output them in a Markdown format. It also
includes the Note and Chapter_notes classes to structure the notes data.
"""

# !/usr/bin/env python3
import os
from collections import OrderedDict

import pyperclip
from bs4 import BeautifulSoup
from eglogging import *

logging_load_human_config()


# -nl, --no-location    -Do not include the source location of each note/highlight
# -c, --clipboard       -Export .md directly to the clipboard instead of file
# -y, --override        -Override .md file if one already exists
# -o OUTPUT, --output   -A file to which save the Markdown document


class Notes:
    """
    This class represents a highlight, possibly including a note, from the Kindle book.
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
    """

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
    """

    def __init__(self):
        """
        Initialize a new instance of the Kindle_notes class.
        """
        self.book_title = ''
        self.author = ''
        self.chapter_notes = []  # list of Chapter_notes

    def parse_file(self, html_file):
        """
        Parse the given HTML file and extract the notes.
        """
        htmls = self._read_file(html_file)
        soup = self._parse_html(htmls)
        all_divs = self._get_all_divs(soup)
        self._process_divs(all_divs)

    @staticmethod
    def _read_file(html_file):
        """
        Read the contents of the given HTML file.
        """
        with open(html_file, 'r', encoding='utf8') as fp:
            htmls = fp.read()
        return htmls

    @staticmethod
    def _parse_html(htmls):
        """
        Parse the given HTML string using BeautifulSoup.
        """
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
        """
        wip_note = None
        last_note_type = ''
        for div in all_divs:
            c = div['class'][0]
            try:
                div_contents = div.get_text().strip().replace(u' \xa0', '')
            except AttributeError as e:
                div_contents = None
                print(f"Error: {e}")
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
        """
        source = ' '.join(div.stripped_strings)
        location = int(source.split()[-1])
        last_note_type = source.split()[0]
        if last_note_type == 'Note':
            try:
                wip_note = self.chapter_notes[-1].get_last_note()
            except Exception as e:
                wip_note = None
                print(f"Error: {e}")
        else:
            wip_note = None
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
        """
        div_contents = div_contents.split('\n')[0]
        if last_note_type == 'Highlight':
            wip_note.text = div_contents
        elif last_note_type == 'Note':
            wip_note.note = div_contents
        return last_note_type, wip_note

    def output_md(self, args):
        """
        Output the notes as a Markdown document.
        """
        md = self._create_md_header()
        md += self._create_md_body(args)
        self._output_md(md, args)

    def _create_md_header(self):
        """
        Create the header for the Markdown document.
        """
        md = "\n\n# {}\n".format(self.book_title)
        md += "- {}\n".format(self.author)
        return md

    def _create_md_body(self, args):
        """
        Create the body for the Markdown document.
        """
        md = ""
        for chapter in self.chapter_notes:
            md += "## {}\n".format(chapter.title)
            for location in chapter.notes:
                note = chapter.notes[location]
                md += "- {}\n".format(note.text)
                if note.note != '':
                    md += "    - **{}**\n".format(note.note)
                if args.location:
                    md += "    - {}\n".format(note.source)
            md += "\n"
        return md

    @staticmethod
    def _output_md(md, args):
        """
        Output the given Markdown string to the appropriate location.
        """
        if args.clipboard:
            pyperclip.copy(md)
            INFO("Copied the output to clipboard", LOG_COLORS['GREEN'])
        else:
            if not os.path.exists(args.output) or args.override:
                with open(args.output, 'w', encoding='utf8') as fp:
                    fp.write(md)
                INFO("Wrote the output to {}".format(args.output), LOG_COLORS['GREEN'])
            else:
                INFO("Could not save .md file, because it already exists. Use --override flag.", LOG_COLORS['RED'])
