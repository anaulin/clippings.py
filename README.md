# clippings.py <!-- omit in toc -->
A Python script to extract book highlights from a Kindle MyClippings.txt file into a structured file.

- [Installation](#installation)
- [Running](#running)
- [Environment and dependencies setup](#environment-and-dependencies-setup)
- [Related work](#related-work)

## Installation

Requires Python 3.

Install dependencies with `pip` or `easy_install`:
```
pip install -r requirements.txt
```

## Running

Extract highlights from MyClippings.txt file to `.csv` spreadsheet:
```
$ ./clippings.py extract MyClippints.txt
```

Full usage:
```
$ ./clippings/clippings.py --help
MyClippings.txt management tool.

Usage:
  clippings.py extract FILE [-o FILE]
  clippings.py (-h | --help)
  clippings.py --version

Options:
  -h --help     Show this screen
  --version     Show version
  -o FILE       Specify output file [default ./clippings.csv]
```

## Environment and dependencies setup

Create new virtual env:
```
python3 -m venv .venv
```

Activate virtual env:
```
source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

## Related work

[kindle-clippings](https://github.com/lvzon/kindle-clippings) is a Python script that processes your `My Clippings.txt` file and outputs clippings as RST files.
