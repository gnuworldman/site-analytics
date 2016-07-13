"""URL configuration for the site_analytics project."""

from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from site_analytics import views


router = routers.DefaultRouter()
router.register('requests', views.RequestViewSet)
router.register('version', views.VersionViewSet, 'version')

urlpatterns = router.urls + [
    url('^summary.html$', views.SummaryView.as_view()),
    url('^filter.html$', views.FilterView.as_view()),
    url('^admin/', admin.site.urls),
]
