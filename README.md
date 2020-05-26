# clippings.py
A Python script to extract book highlights from a Kindle MyClippings.txt into a structured spreadsheet.

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
$ ./clippings.py --help
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
