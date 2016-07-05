"""Transforms for the site_analytics project."""

from django.db.models.fields import URLField
from django.db.models.lookups import Transform


@URLField.register_lookup
class UrlSiteTransform(Transform):

    lookup_name = 'site'

    function = 'url_site'
