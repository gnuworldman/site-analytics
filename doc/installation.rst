Installation
============

Interpreter
-----------

Install the Python 3 interpreter and development libraries.  For example on
Ubuntu::

  sudo apt-get install python3-dev
  sudo apt-get install python3.$(python3 -c 'import sys; print(sys.version_info[1])')-venv

Database
--------

Install the PostgreSQL 9.5 DBMS and its server development library.  For
example on Ubuntu::

  wget -q -O- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/postgresql.list > /dev/null
  sudo apt-get update
  sudo apt-get install postgresql-9.5 postgresql-server-dev-9.5

A PostgreSQL role and database will need to be created for the project to use,
for example on Ubuntu::

  sudo su - postgres -c "createuser -d ${USER}"
  sudo su - postgres -c "createdb -O ${USER} site_analytics"


Virtual environment
-------------------

It is recommended to create and activate a virtual environment.  For example::

  python3 -m venv ~/.virtualenvs/site-analytics
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

  sudo apt-get install git
  git clone https://github.com/gnuworldman/site-analytics.git

Change to the resulting project directory::

  cd site-analytics

It is probably best to run from the project directory at this point (next 
section), but the setup script can be used to install if you really want to::

  ./setup.py install
