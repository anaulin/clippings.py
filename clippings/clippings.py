#!/usr/bin/env python3
"""My Clippings.txt management tool.

Usage:
  clippings.py extract INFILE [-o FILE]
  clippings.py (-h | --help)
  clippings.py --version

Options:
  -o FILE       Specify output file [default ./clippings.csv]
  -h --help     Show this screen
  --version     Show version

"""
import csv
import re

from docopt import docopt

SEPARATOR = "=========="
TITLE_LINE_REGEX = re.compile(r"(.*)\((.*)\)")
ADDED_ON_REGEX = re.compile(r"\| Added on")
YOUR_HIGHLIGHT_ON_REGEX = re.compile(r"- Your Highlight on (.*)")

def get_title_author(line):
    """Returns (title, author) extracted from given line.

    Expects 'line' to be of the form:
    Some Book Title (Author Name)
    ...or...
    Some Book Title
    """
    try:
        if "(" in line and ")" in line:
            title, author = TITLE_LINE_REGEX.match(line).groups()
        else:
            title = line
            author = "Unknown"
        return (title.strip(), author.strip())
    except Exception as err:
        raise ValueError(f"Could not extract title and author from line: {line}. Msg: {err}")

def get_location_date(line):
    """Returns (location, date) extracted from given line.

    Expects 'line' to be of the form:
    - Your Highlight on Location 543-544 | Added on Sunday, May 17, 2020 9:45:47 AM
    ...or...
    - Your Highlight on page 75 | Location 156-157 | Added on Thursday, December 6, 2018 1:02:24 AM
    """
    first_half, date = ADDED_ON_REGEX.split(line)
    if not first_half or not date:
        raise ValueError(f"Could not extract location and date from line: {line}")
    location = YOUR_HIGHLIGHT_ON_REGEX.match(first_half).groups(0)[0]
    return (location.strip(), date.strip())

def add_clipping_to_data(item_name, highlight_lines, location, date, author, data):
    """Adds the given clipping info to the 'data' dict."""
    clipping = {
        'highlight': "\n".join(highlight_lines),
        'location': location,
        'date': date
    }
    if item_name not in data:
        data[item_name] = {'author': author, 'clippings': [clipping]}
    else:
        data[item_name]['clippings'].append(clipping)

def load_file(infile):
    """Loads the clippings data in the given file descriptor.

    Args:
        infile (str): Filename to load data from.

    Returns:
        dict: Structured clippings data loaded from file.
              Format:
              key = item name (e.g. book title)
              value = { author_name, clippings: [{highlight, location, date}] }
    """
    data = {}
    with open(infile, 'r', encoding='utf-8-sig') as inf:
        item_name = author = location = date = None
        highlight_lines = []
        in_highlight = False
        for line in inf:
            if not in_highlight:
                if not line.startswith('- Your Highlight on'):
                    item_name, author = get_title_author(line)
                else:
                    location, date = get_location_date(line)
                    in_highlight = True
            elif line.startswith(SEPARATOR):
                add_clipping_to_data(item_name, highlight_lines, location, date, author, data)
                in_highlight = False
                item_name = author = location = date = None
                highlight_lines = []
            else:
                if line.strip():
                  highlight_lines.append(line.strip())
        if highlight_lines:
            add_clipping_to_data(item_name, highlight_lines, location, date, author, data)
    return data

def write_to_csv(data, outfile):
    """Writes the given data to the outfile."""
    with open(outfile, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Highlight', 'Location', 'Date'])
        for item, values in data.items():
            author = values['author']
            for clipping in values['clippings']:
                writer.writerow([
                    item, author, clipping['highlight'], clipping['location'], clipping['date']])


def extract(infile, outfile):
    """Extract the contents of infile into outfile."""
    print(f"Extracting {infile} into {outfile}")
    clippings = load_file(infile)
    print(f"Extracted clippings from {len(clippings.keys())} books")
    write_to_csv(clippings, outfile)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='My Clippings.txt Manager v0.1')
    if arguments['extract']:
        extract(arguments['INFILE'], arguments['-o'] or './clippings.csv')
