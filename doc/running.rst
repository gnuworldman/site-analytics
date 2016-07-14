Running
=======

Prerequisites
-------------

A virtual environment is recommended.  Ensure that it is activated (e.g., shell
prompt begins with ``(site-analytics)``).

If you want to run the service without installing it, then the dependencies
must be installed::

  pip install -Ur "{{ project_root }}/requirements.txt"

Prepending "sudo " to that command might be necessary if not using a virtual
environment.

The static files for all of the apps in the project must be collected, and the
database must be initialized/migrated::

  export PYTHONPATH="{{ project_root }}/src"
  "$PYTHONPATH/src/site_analytics/manage.py" collectstatic --noinput
  "$PYTHONPATH/src/site_analytics/manage.py" migrate

Start the service
-----------------

Add the project to the Python path and execute::

  export PYTHONPATH="{{ project_root }}/src"
  "$PYTHONPATH/site_analytics/manage.py" runserver

See the help for the ``runserver`` command to control the service port, etc.
