"""Managers for the site_analytics project."""

from collections import OrderedDict

from django.conf import settings
from django.db import connection
from django.db.models import Manager


def quote_ident(identifier):
    """Quote an SQL identifier.

    Replace this with psycopg2.extensions.quote_ident
    (`pull request <https://github.com/psycopg/psycopg2/pull/359>`_)
    when it gets into a stable release.

    """
    return '"{}"'.format(identifier.replace('"', '""'))


class RequestManager(Manager):

    @property
    def data_column(self):
        field = self.model._meta.get_field('data')
        return field.db_column or field.name

    def get_user_field_expr(self, user_field):
        return "{}#>'{{user,{}}}'".format(quote_ident(self.data_column),
                                          user_field.replace('__', ','))

    def get_user_count(self, user_field):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(DISTINCT({})) FROM {}"
                .format(self.get_user_field_expr(user_field),
                        quote_ident(self.model._meta.db_table)))
            return cursor.fetchone()[0]

    def get_user_counts(self, user_field):
        field_expr = self.get_user_field_expr(user_field)
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT DISTINCT({0}), COUNT(1) AS c FROM {1}"
                " WHERE {0} IS NOT NULL GROUP BY {0}"
                " ORDER BY c DESC LIMIT %s"
                .format(field_expr, quote_ident(self.model._meta.db_table)),
                (settings.SITEANALYTICS_DASHBOARD_TOP_N,))
            return OrderedDict(cursor.fetchall())
