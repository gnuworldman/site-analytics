User Interface
==============

In addition to the API, there are also some user interfaces provided to
interact with the system at the same scheme/host/port as the API.

Summary page
------------

The summary page contains totals and counts of the top values of certain
categories of data.  View the page by browsing to the ``/summary.html`` path.

Filter page
------------

The filter page contains a form to enter the same query data as is accepted by
the ``/requests`` collection.  View the page by browsing to the
``/filter.html`` path.  Enter complete values in one or more fields and click
the ``Submit Query`` button to see a list of requests that match the criteria.

The "Timestamp" input fields are ``from`` and ``to``; they are inclusive, and
any number of the two fields may be entered, but if one has a value, then it
must be a complete date and time in ISO-8601 format.

Create a user
-------------

A superuser (and optionally any further desired users) is required to access
the Admin or Browsable-API interfaces.  To create a superuser (make sure that
the virtual environment is activated)::

  export PYTHONPATH="{{ project_root }}/src"
  "{{ project_root }}/src/site_analytics/manage.py" createsuperuser

Then, one can login to the Admin with the superuser to create any additional
users.

Admin
-----

The Django "Admin" interface provides direct access to persisted objects.  Use
the path ``/admin`` to access this interface.

Browsable API
-------------

The REST Framework's "Browsable API" is disabled by default but can be enabled
by putting into settings_local.py the code from the comment under
``REST_FRAMEWORK`` in settings.py.  This is like the "Admin" except that it is
for views (at the API endpoints) rather than for models.
