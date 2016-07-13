"""Filters for the site_analytics project."""

from django.core.exceptions import ValidationError
from django_filters import fields, filters, filterset
from rest_framework import exceptions

from site_analytics import models


class IsoDateTimeRangeField(fields.RangeField):

    """Field for a datetime range in ISO-8601 format."""

    def __init__(self, *args, **kwargs):
        super().__init__((fields.IsoDateTimeField(),
                          fields.IsoDateTimeField()),
                         *args, **kwargs)


class IsoDateTimeFromToRangeFilter(filters.DateTimeFromToRangeFilter):

    """Filter for a datetime range in ISO-8601 format."""

    field_class = IsoDateTimeRangeField


class RequestFilter(filterset.FilterSet):

    """Set of filters for the `~site_analytics.models.Request` model.

    The ``site`` parameter can be used to filter requests that have a
    ``url`` within the site (scheme & authority) argument.

    The ``timestamp_0`` parameter can be used to filter requests that
    were made on or after the argument.  The ``timestamp_1`` parameter
    can be used to filter requests that were made on or before the
    argument.  Values for each of these parameters must be in ISO-8601
    date/time format.

    The ``username`` parameter can be used to filter requests that were
    made by the user identified by the argument.

    The ``ip_address`` parameter can be used to filter requests that were
    made from the specified IP address.

    The ``state`` parameter can be used to filter requests that were made
    from the specified state (two-character upper-case abbreviation).
    This value resides in the ``region`` field of the object in the
    ``geoip`` field of the object in the ``user`` field.

    """

    strict = filterset.STRICTNESS.RAISE_VALIDATION_ERROR

    site = filters.CharFilter(name='url', lookup_expr='site')
    timestamp = IsoDateTimeFromToRangeFilter()
    username = filters.CharFilter(name='data', lookup_expr='user__name')
    ip_address = filters.CharFilter(name='data',
                                    lookup_expr='user__ip_address')
    state = filters.CharFilter(name='data', lookup_expr='user__geoip__region')

    class Meta:

        model = models.Request
        fields = 'url', 'site', 'timestamp', 'username', 'ip_address', 'state'

    @property
    def qs(self):
        """Override to produce a REST Framework ValidationError."""
        try:
            return super().qs
        except ValidationError as exc:
            raise exceptions.ValidationError(exc.error_dict)
