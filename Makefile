.PHONY: install lab test

install:
	pip install -r requirements.txt

lab:
	jupyter lab

test:
	pytest -q
