# Makefile for the site_analytics project
# This has only been tested with GNU make from within the project root.

SHELL := /bin/bash

all: coverage build doc

flake:
	flake8 src

test: flake
	PYTHONPATH=src coverage run src/site_analytics/manage.py test site_analytics --noinput

coverage: test
	coverage report --fail-under=100

coverage_html: test
	coverage html

build:
	./setup.py build

readme:
	cat README_editable.rst | ( while read; do if [[ $${REPLY#.. include:: } != $${REPLY} ]]; then cat $${REPLY#.. include:: }; else echo $${REPLY}; fi; done ) > README.rst

doc: readme
	sphinx-apidoc -M -e -f -o doc src/site_analytics
	$(MAKE) -C doc html

deb:
	./setup.py --command-packages=stdeb.command sdist_dsc --with-python2=False --with-python3=True bdist_deb

clean:
	./setup.py clean -a
	$(MAKE) -C doc clean
	$(RM) MANIFEST
	$(RM) -r dist
	$(RM) -r src/*.egg-info
	$(RM) -r htmlcov
	coverage erase
	find . -type d -name '__pycache__' | xargs $(RM) -r
	find . -type f -name '*.py[co]' | xargs $(RM)

.PHONY: test coverage coverage_html build readme doc clean deb
