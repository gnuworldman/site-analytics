"""Models for the site_analytics project."""

from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.postgres.fields import jsonb
from django.db import models
from django.utils.timezone import now
from geoip2.errors import AddressNotFoundError

from site_analytics import managers
# Load and register Transform classes.
from site_analytics import transforms  # noqa


USER_GEOIP_KEY = 'geoip'


class Request(models.Model):

    """A request whose details are sent by the service processing it.

    A service that processes an incoming request posts to this service,
    which persists the posted data via this model.

    The requested URL (the :attr:`url` field) is required.  The
    timestamp field may be specified and defaults to the current time.
    The remainder of posted data goes into the :attr:`data` field.  If
    the user is identified in any way by the processing service, then
    that data should be specified as an object in the ``user`` field.
    If the client IP address is known and should be saved, then it
    should be specified in the `ip_address` field of the user object.
    If the U.S. state of the origin of the request is known and should
    be saved, then it should be specified in the ``region`` field of
    the object in the ``geoip`` field in the user object, but it is
    easier for the client to specify the IP address and let the system
    fill in the ``geoip`` field of the user object based on that.  If
    the request was made by a particular user and should be saved, then
    the username should be specified in the ``name`` field of the user
    object.  These three special fields of the user object can be used
    to filter requests with query parameters to a GET on the requests
    collection; see `~site_analytics.filters.RequestFilter` for
    details.

    If ``ip_address`` is provided in the user object and ``geoip`` is
    not, then the ``geoip`` field in the user object is populated with
    GeoIP data based on the given IP address if its location can be
    determined.

    """

    url = models.URLField(
        max_length=2000,
        db_index=True,
        help_text="The absolute URL of the request")

    timestamp = models.DateTimeField(
        default=now,
        db_index=True,
        help_text="The time at which the request was made")

    data = jsonb.JSONField(
        blank=True,
        default=dict,
        help_text="Additional data related to the request")

    class Meta:

        db_table = 'request'

    objects = managers.RequestManager()

    @classmethod
    def get_data_column(cls):
        """Return the database column name for the :attr:`data` field."""
        field = cls._meta.get_field('data')
        return field.db_column or field.name

    def __str__(self):
        if self.pk:
            return "Request {}".format(self.pk)
        return super().__str__()

    def clean(self):
        self.set_geoip_data()
        return super().clean()

    def set_geoip_data(self):
        """Use the IP address, if provided, to look up and store GeoIP data.

        Respect any provided geoip value by not overwriting it.

        """
        if not self.data:
            return
        try:
            user = self.data['user']
        except KeyError:
            return
        if USER_GEOIP_KEY in user:
            # Do not overwrite explicitly set data.
            return
        try:
            ip_address = user['ip_address']
        except KeyError:
            return
        try:
            user[USER_GEOIP_KEY] = GeoIP2().city(ip_address)
        except AddressNotFoundError:
            pass
