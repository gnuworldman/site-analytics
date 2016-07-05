"""Models for the site_analytics project."""

from django.db import models
from django.contrib.postgres.fields import jsonb
from django.utils.timezone import now

# Load and register Transform classes.
from site_analytics import transforms  # noqa


class Request(models.Model):

    """A request whose details are sent by the service processing it.

    A service that processes an incoming request posts to this service,
    which persists the posted data via this model.

    The requested URL (the :attr:`url` field) is required.  The
    timestamp field may be specified and defaults to the current time.
    The remainder of posted data goes into the :attr:`data` field.  If
    the user is identified in any way by the processing service, then
    that data should be specified as an object in the `user` field.  If
    the client IP address is known and should be saved, then it should
    be specified in the `ip_address` field of the user object.  If the
    U.S. state of the origin of the request is known and should be
    saved, then it should be specified in the `state` field of the user
    object.  If the request was made by a particular user and should be
    saved, then the username should be specified in the `name` field of
    the user object.  These three special fields of the user object can
    be used to filter requests with query parameters to a GET on the
    requests collection; see `~site_analytics.filters.RequestFilter`
    for details.

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
        db_index=True,
        help_text="Additional data related to the request")

    class Meta:

        db_table = 'request'

    def __str__(self):
        if self.pk:
            return "Request {}".format(self.pk)
        return super().__str__()
