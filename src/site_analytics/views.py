"""Views for the site_analytics project."""

from rest_framework import mixins, response, viewsets

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
