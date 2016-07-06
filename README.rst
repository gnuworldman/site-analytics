Site Analytics is a RESTful API service that persists and retrieves data
related to requests.  The best way to use it is to have the services that are
processing web requests post all pertinent information about the requests to
this service where the data is persisted and can then be retrieved and filtered
to gain analytical insights.

The `source <https://github.com/gnuworldman/site-analytics/tree/master>`_,
`documentation <http://gnuworldman.github.io/site-analytics/>`_,
and `issues <https://github.com/gnuworldman/site-analytics/issues>`_
are hosted on `GitHub <https://github.com/>`_.

.. image:: https://travis-ci.org/gnuworldman/site-analytics.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/gnuworldman/site-analytics

.. image:: https://img.shields.io/coveralls/gnuworldman/site-analytics.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/gnuworldman/site-analytics?branch=master

Overview
========

This API allows sites to persist and query client requests.
