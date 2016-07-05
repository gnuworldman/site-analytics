"""The initial migration for the site_analytics project."""

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


SQL_FUNCTION_URL_SITE = dict(
    create="""CREATE OR REPLACE FUNCTION url_site(url VARCHAR)
RETURNS VARCHAR
LANGUAGE plpgsql
IMMUTABLE
RETURNS NULL ON NULL INPUT
AS $$
BEGIN
    RETURN SUBSTRING(url FROM '^[^:]+://[^/]+');
END;
$$;""",
    drop="""DROP FUNCTION url_site(VARCHAR);""",
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('url', models.URLField(
                    db_index=True,
                    help_text='The absolute URL of the request',
                    max_length=2000)),
                ('timestamp', models.DateTimeField(
                    db_index=True,
                    default=django.utils.timezone.now,
                    help_text='The time at which the request was made')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(
                    blank=True,
                    default=dict,
                    help_text='Additional data related to the request')),
            ],
            options={
                'db_table': 'request',
            },
        ),
        migrations.RunSQL(
            SQL_FUNCTION_URL_SITE['create'],
            SQL_FUNCTION_URL_SITE['drop']
        ),
        migrations.RunSQL(
            "CREATE INDEX request_data_index ON request USING GIN (data);",
            "DROP INDEX request_data_index;"
        ),
        migrations.RunSQL(
            "CREATE INDEX request_url_site ON request (url_site(url));",
            "DROP INDEX request_url_site;"
        ),
    ]
