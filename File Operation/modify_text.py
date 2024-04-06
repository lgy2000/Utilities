import os
from datetime import datetime

from config import input_text, to_add_title, to_remove_prefix, to_add_prefix, to_add_suffix, to_change_case
from get_title_from_file import main as get_title


def remove_prefix(to_remove_prefix, text, delimiter=" "):
    if to_remove_prefix == 1:
        parts = text.split(delimiter)
        if len(parts) > 1:
            return delimiter.join(parts[1:])
    return text


def add_prefix(to_add_prefix, text, counter, prefix_str):
    """return the prefix"""
    if to_add_prefix == 0:
        return ""
    elif to_add_prefix == 1:
        return f"{counter} "
    elif to_add_prefix == 2:
        return f"{datetime.fromtimestamp(os.stat(text).st_mtime)} "
    elif to_add_prefix == 3:
        return f"{prefix_str} "


def add_suffix(to_add_suffix, text, counter, suffix_str):
    """return the suffix"""
    if to_add_suffix == 0:
        return ""
    elif to_add_suffix == 1:
        return f" {counter}"
    elif to_add_suffix == 2:
        return f" {datetime.fromtimestamp(os.stat(text).st_mtime)}"
    elif to_add_suffix == 3:
        return f" {suffix_str}"

def add_title(to_add_title):
    if to_add_title == 1:
        return get_title()
    else:
        return ""

def change_case(to_change_case, text):
    """return the text in selected case"""
    if to_change_case == 1:
        return title_case(text)
    elif to_change_case == 2:
        return text.upper()
    elif to_change_case == 3:
        return text.lower()
    return text


def title_case(text):
    """return the text in title case"""
    # List of small words to exclude from capitalization
    small_words = ['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'if', 'in', 'nor', 'of', 'on', 'or', 'so', 'the',
                   'to', 'up', 'yet']

    # Split the text into words
    words = text.split()

    # Convert the first letter of each word to uppercase, unless it's a small word and not the first word
    title_words = [word.capitalize() if word.lower() not in small_words or index == 0 else word for index, word in
                   enumerate(words)]

    # Join the title case words back into a string
    return ' '.join(title_words)


def main():
    counter = ""
    prefix_str = ""
    suffix_str = ""

    text = remove_prefix(to_remove_prefix, input_text, delimiter=" ")
    prefix = add_prefix(to_add_prefix, text, counter, prefix_str)
    suffix = add_suffix(to_add_suffix, text, counter, suffix_str)
    title = add_title(to_add_title)
    text = f"{prefix}{text}{suffix}{title}"
    text = change_case(to_change_case, text)

    print(text)
    return text


if __name__ == '__main__':
    main()
