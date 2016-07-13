Release Notes
=============

Version 0.2.0
-------------

Add GeoIP data according to the IP address.  This breaks compatibility with the
previous version as the old user->state field is now user->geoip->region.

Add a crude, yet useful user interface with /summary.html and /filter.html.

Version 0.1.0
-------------

Implement and unit-test the API.
