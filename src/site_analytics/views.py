"""Views for the site_analytics project."""

from rest_framework import mixins, renderers, response, views, viewsets

from site_analytics._version import __version__
from site_analytics import filters, models, serializers


class VersionViewSet(viewsets.ViewSet):

    """A GET on /version returns the version string.

    A `ViewSet` is used for its automatic routing features, but the
    ``list`` method is the only one implemented and returns an entity
    that is not a collection, for which `ViewSet`\s are normally used.

    """

    def list(self, request, *args, **kwargs):
        """Return the service's version number."""
        return response.Response(__version__)


class RequestViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    """The view set used for the /requests collection."""

    queryset = models.Request.objects.order_by('-timestamp', '-id')
    serializer_class = serializers.RequestSerializer
    filter_class = filters.RequestFilter

    # TODO: Add security; limit results to user's own requests if non-staff.
    # This assumes that authentication is shared among all services.
    # To see any unauthenticated requests (no user or no name in user), the
    # user would have to be staff.

#     # from rest_framework import permissions
#     permission_classes = permissions.IsAuthenticated,
#
#     def get_queryset(self):
#         result = super().get_queryset()
#         user = self.request.user
#         if not user.is_staff:
#             result = result.filter(data__user__name=user.username)
#         return result


class SummaryView(views.APIView):

    renderer_classes = renderers.TemplateHTMLRenderer,
    template_name = 'site_analytics/summary.html'

    def get(self, request, *args, **kwargs):  # pragma: no cover
        manager = models.Request.objects
        data = dict(
            totals=dict(
                requests=manager.count(),
                auth_users=manager.get_user_count('name'),
                states=manager.get_user_count('geoip__region'),
                ip_addresses=manager.get_user_count('ip_address'),
            ),
            tops=dict(
                auth_users=manager.get_user_counts('name'),
                states=manager.get_user_counts('geoip__region'),
                ip_addresses=manager.get_user_counts('ip_address'),
            ),
        )
        return response.Response(data)


class FilterView(views.APIView):

    renderer_classes = renderers.TemplateHTMLRenderer,
    template_name = 'site_analytics/filter.html'

    def get(self, request, *args, **kwargs):  # pragma: no cover
        show_data = bool(request.query_params)
        qs = models.Request.objects.all()
        filter_ = filters.RequestFilter(request.query_params, qs)
        if show_data:
            show_data = filter_.form.is_valid()
        # The form and show_data variables are passed in to work around errors
        # related to validation, strictness, and template variable dot lookups.
        # If the template used {{ filter.form }}, then it would attempt
        # filter['form'] before filter.form, and filter.__getitem__('form')
        # could raise an error if the form is invalid.  Similarly, show_data
        # is used instead of {{ filter|length }}.
        data = dict(filter=filter_, form=filter_.form, show_data=show_data)
        return response.Response(data)
