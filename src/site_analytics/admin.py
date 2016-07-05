"""Admin configuration for the site_analytics project."""

from django.contrib import admin

from site_analytics import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):

    class Meta:

        model = models.Request
