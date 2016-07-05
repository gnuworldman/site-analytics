Request information
===================

Each request contains at least the following fields:
	
url
  the request's absolute URL
	
timestamp
  the time at which the request was made or persisted

Any additional fields related to the request are stored in the
:attr:`~site_analytics.models.Request.data`
(`jsonb <https://www.postgresql.org/docs/9.5/static/datatype-json.html>`_)
field.  See the :class:`~site_analytics.models.Request` model docstring for
pertinent information regarding the request entity's ``user`` field.

When persisted requests are retrieved, a field called ``self`` that contains 
the URL of the request resource is also included.

API calls
=========

POST /requests
--------------

Store the details related to a request.  The ``url`` field is required, and the
``timestamp`` field defaults to the current date and time.  Any other fields in
the payload are also persisted.

GET /requests
-------------

Return a pagination object (default page size is 10) with the following fields:

count
  the total number of (matching, if filtered) requests

previous
  the URL of the previous page (`null` if this is the first page)

next
  the URL of the next page (`null` if this is the last page)

results
  array of (matching, if filtered) stored requests on this page -- each element
  is the same object as returned by calling the GET method on the entity's URL
  (``self`` field)

This call supports filtering with query parameters.  See
`~site_analytics.filters.RequestFilter` for details.

GET /requests/{id}
------------------

Return an object with all of the data given when the request was persisted
along with the ``self`` field.

GET /version
------------

Return a string containing the version number of the service.
