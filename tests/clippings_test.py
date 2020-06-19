"""Basic end-to-end tests for clippings.py."""

import tempfile
import csv
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from clippings import clippings

TEST_INFILE = os.path.join(os.path.dirname(__file__), "Test_Clippings.txt")


def get_csv_lines(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        return list(reader)


def test_extract():
    with tempfile.NamedTemporaryFile() as temp:
        clippings.extract(TEST_INFILE, temp.name)
        result = get_csv_lines(temp.name)
        assert len(result) == 11
        assert result[0] == ['Title', 'Author', 'Highlight', 'Location', 'Date']
        for row in result[1:]:
            assert row[2].startswith('\n') == False
