"""Serializers for the site_analytics project."""

from rest_framework import serializers

from site_analytics import models


class RequestSerializer(serializers.HyperlinkedModelSerializer):

    """The serializer for the `~site_analytics.views.RequestViewSet`."""

    STATIC_FIELDS = 'self', 'url', 'timestamp'

    class Meta:

        model = models.Request

    def to_internal_value(self, data):
        new_data = {}
        for key in self.STATIC_FIELDS:
            try:
                new_data[key] = data.pop(key)
            except KeyError:
                pass
        new_data.update(data=data)
        return super().to_internal_value(new_data)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        data = result['data']
        result = {x: result[x] for x in self.STATIC_FIELDS}
        result.update(data)
        return result
