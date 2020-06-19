.DEFAULT: extract

.PHONY: extract
extract:
	source .venv/bin/activate && ./clippings/clippings.py extract /Volumes/Kindle/documents/My\ Clippings.txt

.PHONY: lint
lint:
	pylint ./clippings/*.py tests/*.py

.PHONY: autopep8
autopep8:
	autopep8 --in_place $(file)

.PHONY: test
test:
	pytest
