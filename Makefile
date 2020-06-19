.DEFAULT: extract

.PHONY: extract
extract:
	source .venv/bin/activate && ./clippings.py extract /Volumes/Kindle/documents/My\ Clippings.txt
