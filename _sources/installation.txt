Installation
============

Prerequisites
-------------

Install the Python 3.5 and PostgreSQL 9.5 development libraries.  For example
on Ubuntu::

  sudo apt-get install python3.5-dev python3.5-venv
  sudo apt-get install postgresql-9.5 postgresql-server-dev-9.5

Virtual environment
-------------------

It is recommended to create and activate a virtual environment.  For example::

  pyvenv-3.5 ~/.virtualenvs/site-analytics
  source ~/.virtualenvs/site-analytics/bin/activate


.. Uncomment if the project gets published on PyPI:
	Via pip
	-------
	
	If a stable release is desired, pip is the way to go.
	
	The Site Analytics application can be installed easily with pip::
	
	  pip install site-analytics

Via source
----------

.. Uncomment if the project gets published on PyPI:
	The source can be used to install if one is developing modifications or
	requires the latest unreleased changes.

Get the source::

  git clone https://github.com/gnuworldman/site-analytics.git

Change to the resulting project directory::

  cd site-analytics

It is probably best to run from the project directory at this point (next 
section), but the setup script can be used to install if you really want to::

  ./setup.py install
