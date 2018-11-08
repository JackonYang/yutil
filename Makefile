PY?=python3
PIP?=pip3

build:
	$(PY) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

install:
	$(PIP) install -e .

unittest:
	pytest .

.PHONY: build upload install
.PHONY: unittest
