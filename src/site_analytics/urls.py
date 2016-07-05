"""URL configuration for the site_analytics project."""

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django_filters.views import FilterView
from rest_framework import routers

from site_analytics import filters, views


router = routers.DefaultRouter()
router.register('requests', views.RequestViewSet)
router.register('version', views.VersionViewSet, 'version')

urlpatterns = router.urls + [
    url('^filter.html$',
        FilterView.as_view(filterset_class=filters.RequestFilter)),
]
if settings.DEBUG:  # pragma: nocover
    urlpatterns.append(url('^admin/', admin.site.urls))
