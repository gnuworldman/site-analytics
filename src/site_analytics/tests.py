"""Tests for the site_analytics project."""

import datetime
from urllib.parse import urlparse

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from pytz import UTC
from rest_framework import status
from rest_framework.test import APITestCase

from site_analytics import models
from site_analytics._version import __version__


class RequestModelTestCase(TestCase):

    def create_request(self, **data):
        obj = models.Request(**data)
        obj.full_clean()
        obj.save()
        return obj

    def test_str(self):
        obj = models.Request(url='https://host.net/')
        obj.full_clean()
        self.assertEqual("Request object", str(obj))
        obj.save()
        self.assertEqual("Request {}".format(obj.pk), str(obj))

    def test_set_geoip_data(self):
        obj = self.create_request(url='https://host.net/',
                                  data=dict(user=dict(ip_address='9.8.7.6')))
        self.assertEqual('NC', obj.data['user']['geoip']['region'])

    def test_set_geoip_data_private_address(self):
        obj = self.create_request(url='https://host.net/',
                                  data=dict(user=dict(ip_address='10.1.1.2')))
        self.assertNotIn('geoip', obj.data['user'])

    def test_set_geoip_data_no_user(self):
        obj = self.create_request(url='https://host.net/',
                                  data=dict(other='stuff'))
        self.assertNotIn('user', obj.data)

    def test_set_geoip_data_no_ip_address(self):
        obj = self.create_request(url='https://host.net/',
                                  data=dict(user=dict(name='oscar')))
        self.assertNotIn('geoip', obj.data['user'])

    def test_set_geoip_data_do_not_overwrite(self):
        obj = self.create_request(url='https://host.net/',
                                  data=dict(user=dict(name='oscar',
                                                      geoip=42)))
        self.assertEqual(42, obj.data['user']['geoip'])

    def test_get_user_count(self):
        self.assertEqual(0, models.Request.objects.get_user_count('name'))
        self.create_request(url='https://host.net/',
                            data=dict(user=dict(name='arnold')))
        self.assertEqual(1, models.Request.objects.get_user_count('name'))
        self.create_request(url='https://host.net/',
                            data=dict(user=dict(name='mary')))
        self.assertEqual(2, models.Request.objects.get_user_count('name'))
        self.create_request(url='https://host1.net/')
        self.assertEqual(2, models.Request.objects.get_user_count('name'))
        self.create_request(url='https://host1.net/',
                            data=dict(user=dict(name='arnold')))
        self.assertEqual(2, models.Request.objects.get_user_count('name'))

    def test_get_user_counts(self):
        self.assertDictEqual(dict(),
                             models.Request.objects.get_user_counts('name'))
        self.create_request(url='https://host.net/',
                            data=dict(user=dict(name='arnold')))
        self.assertDictEqual(dict(arnold=1),
                             models.Request.objects.get_user_counts('name'))
        self.create_request(url='https://host.net/',
                            data=dict(user=dict(name='mary')))
        self.assertDictEqual(dict(arnold=1, mary=1),
                             models.Request.objects.get_user_counts('name'))
        self.create_request(url='https://host1.net/')
        self.assertDictEqual(dict(arnold=1, mary=1),
                             models.Request.objects.get_user_counts('name'))
        self.create_request(url='https://host1.net/',
                            data=dict(user=dict(name='arnold')))
        self.assertDictEqual(dict(arnold=2, mary=1),
                             models.Request.objects.get_user_counts('name'))


class BaseAPITestCase(APITestCase):

    @staticmethod
    def get_url_base(response):
        env = response.wsgi_request.environ
        return '{}://{}'.format(env['wsgi.url_scheme'], env['SERVER_NAME'])

    def assertTimestamp(self, value):
        result = parse_datetime(value)
        self.assertIsNotNone(result, "Timestamp is not parsable.")
        return result

    def assertRecentTimestamp(self, value, seconds=5):
        value = self.assertTimestamp(value)
        current = now()
        recent = current - datetime.timedelta(seconds=seconds)
        self.assertTrue(recent <= value <= current)


class VersionAPITestCase(BaseAPITestCase):

    def test_get(self):
        response = self.client.get(reverse('version-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(__version__, response.data)


class RequestAPITestCase(BaseAPITestCase):

    def test_post(self):
        path = reverse('request-list')
        data = dict(url='https://host.net/login.html')
        response = self.client.post(path, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code,
                         response.content)
        location = urlparse(response['Location']).path
        actual = response.data
        self.assertIsInstance(actual, dict)
        actual_location = urlparse(actual.pop('self')).path
        self.assertEqual(location, actual_location)
        self.assertRecentTimestamp(actual.pop('timestamp'))
        self.assertDictEqual(data, actual)
        obj = models.Request.objects.get()
        expected = '{}/{}/'.format(path.rstrip('/'), obj.pk)
        self.assertEqual(expected, location)
        expected = data.copy()
        self.assertEqual(expected.pop('url'), obj.url)
        self.assertEqual(expected, obj.data)

    def test_post_with_data(self):
        path = reverse('request-list')
        data = dict(url='https://host.net/index.html',
                    user='me')
        response = self.client.post(path, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code,
                         response.content)
        location = urlparse(response['Location']).path
        actual = response.data
        self.assertIsInstance(actual, dict)
        actual_location = urlparse(actual.pop('self')).path
        self.assertEqual(location, actual_location)
        self.assertTrue(actual.pop('timestamp'))
        self.assertDictEqual(data, actual)
        obj = models.Request.objects.get()
        expected = '{}/{}/'.format(path.rstrip('/'), obj.pk)
        self.assertEqual(expected, location)
        expected = data.copy()
        self.assertEqual(expected.pop('url'), obj.url)
        self.assertTrue(obj.timestamp)
        self.assertDictEqual(expected, obj.data)

    def test_post_invalid_missing_url(self):
        data = dict(not_url='https://host.net/login.html')
        response = self.client.post(
            reverse('request-list'),
            data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        expected = dict(url=["This field is required."])
        self.assertDictEqual(expected, response.data)

    def test_post_invalid_url(self):
        data = dict(url='This is a malformed URL.')
        response = self.client.post(
            reverse('request-list'),
            data=data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        expected = dict(url=["Enter a valid URL."])
        self.assertDictEqual(expected, response.data)

    def test_get(self):
        # get empty collection
        path = reverse('request-list')
        response = self.client.get(path)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual([], response.data['results'])

        # create first entity
        obj = models.Request.objects.create(
            url='https://host.net/index.html',
            data=dict(user='me'))

        # get collection with one entity
        response = self.client.get(path)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        actual = response.data['results']
        for entity in actual:
            self.assertRecentTimestamp(entity.pop('timestamp'))
        path = reverse('request-detail', kwargs=dict(pk=obj.pk))
        expected = dict(
            obj.data,
            self=self.get_url_base(response) + path,
            url=obj.url)
        self.assertEqual([expected], actual)

        # get entity
        response = self.client.get(path)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        actual = response.data
        self.assertRecentTimestamp(actual.pop('timestamp'))
        self.assertDictEqual(expected, actual)

        # create second entity
        obj = models.Request.objects.create(
            url='https://host.net/index.html',
            data=dict(
                user=dict(id=666, name="Montgomery Burns"),
                tag='Batman'))

        # get collection with multiple entities
        response = self.client.get(reverse('request-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        actual = response.data['results']
        for entity in actual:
            self.assertRecentTimestamp(entity.pop('timestamp'))
        path = reverse('request-detail', kwargs=dict(pk=obj.pk))
        expected = [
            dict(
                obj.data,
                self=self.get_url_base(response) + path,
                url=obj.url),
            expected,
        ]
        self.assertEqual(expected, actual)

        # get second entity
        response = self.client.get(path)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        actual = response.data
        self.assertRecentTimestamp(actual.pop('timestamp'))
        self.assertDictEqual(expected[0], actual)


class RequestQueryTestCase(BaseAPITestCase):

    sites = (
        'https://host1.net',
        'https://host2.net',
        'https://host3.net',
        'https://host4.net',
    )

    addresses = (
        dict(ip_address='10.1.1.1', geoip=dict(region='NC')),
        dict(ip_address='10.1.1.2', geoip=dict(region='NC')),
        dict(ip_address='10.1.1.3', geoip=dict(region='MA')),
    )

    users = (
        dict(name='bob', **addresses[0]),
        dict(name='sue', **addresses[0]),
        dict(name='jack', **addresses[0]),
        dict(name='bill', **addresses[1]),
        dict(name='jill', **addresses[2]),
        dict(name='terry', **addresses[2]),
    )

    request_data = (
        dict(url=sites[0] + '/login.html',
             timestamp='2000-01-01T00:00:00.000000Z'),
        dict(url=sites[0] + '/index.html',
             timestamp='2000-01-01T00:00:00.300000Z',
             user=users[0]),
        dict(url=sites[1] + '/widgets/',
             timestamp='2000-01-01T00:00:03.000000Z',
             user=users[0]),
        dict(url=sites[0] + '/login.html',
             timestamp='2000-01-01T00:12:00.000000Z'),
        dict(url=sites[0] + '/index.html',
             timestamp='2000-01-01T00:12:00.300000Z',
             user=users[1]),
        dict(url=sites[1] + '/things/',
             timestamp='2000-01-01T00:15:00.000000Z',
             user=users[0]),
        dict(url=sites[1] + '/widgets/',
             timestamp='2000-01-01T04:15:00.000000Z',
             user=users[4]),
        dict(url=sites[1] + '/widgets/',
             timestamp='2000-01-01T05:15:00.000000Z',
             user=users[5]),
        dict(url=sites[1] + '/midgets/',
             timestamp='2000-01-01T06:15:00.000000Z',
             user=users[1]),
        dict(url=sites[1] + '/resources/',
             timestamp='2000-01-02T00:10:00.000000Z',
             user=users[3]),
        dict(url=sites[3] + '/order.html',
             timestamp='2000-01-02T00:11:00.000000Z',
             user=users[4]),
        dict(url=sites[2] + '/widgets/',
             timestamp='2000-01-02T00:12:00.000000Z',
             user=users[3]),
        dict(url=sites[1] + '/resources/283907/',
             timestamp='2015-04-03T02:01:00.000000Z',
             user=users[3]),
        dict(url=sites[0] + '/stuff',
             timestamp='2015-04-03T02:01:00.100000Z',
             user=users[2]),
        dict(url=sites[0] + '/index.html',
             timestamp='2015-04-03T02:01:00.100000Z',
             user=users[5]),
        dict(url=sites[3] + '/cart.html',
             timestamp='2015-04-03T02:01:00.500000Z',
             user=users[3]),
        dict(url=sites[3] + '/order.html',
             timestamp='2015-04-03T02:01:00.600000Z',
             user=users[3]),
        dict(url=sites[0] + '/login.html',
             timestamp='2015-04-03T02:01:00.700000Z',
             user=users[4]),
        dict(url=sites[1] + '/resources/',
             timestamp='2015-04-03T02:01:00.800000Z',
             user=users[4]),
        dict(url=sites[0] + '/page.html',
             timestamp='2015-04-03T22:11:00.826391Z',
             user=users[1]),
    )

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.requests = []
        for data in cls.request_data:
            data = data.copy()
            url = data.pop('url')
            timestamp = data.pop('timestamp', None)
            request = models.Request(url=url, timestamp=timestamp, data=data)
            request.full_clean()
            request.save()
            cls.requests.append(request)

    @property
    def path(self):
        return reverse('request-list')

    def test_pagination(self):
        response = self.client.get(self.path)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(len(self.request_data), response.data['count'])
        self.assertIsNone(response.data['previous'])
        self.assertIsNotNone(response.data['next'])

    # TODO: Determine whether to make the API error on invalid parameter.
#     def test_filter_invalid(self):
#         data = dict(invalid='x')
#         response = self.client.get(self.path, data)
#         self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_filter_url(self):
        data = dict(url=self.sites[0] + '/login.html')
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(3, response.data['count'])
        for result in response.data['results']:
            self.assertEqual(result['url'], data['url'])

    def test_filter_site(self):
        data = dict(site=self.sites[0])
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(8, response.data['count'])
        for result in response.data['results']:
            self.assertTrue(result['url'].startswith(data['site']))

    def test_filter_username(self):
        data = dict(username=self.users[0]['name'])
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(3, response.data['count'])
        for result in response.data['results']:
            self.assertEqual(result['user']['name'], data['username'])

    def test_filter_ip_address(self):
        data = dict(ip_address=self.addresses[0]['ip_address'])
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(7, response.data['count'])
        for result in response.data['results']:
            self.assertEqual(result['user']['ip_address'], data['ip_address'])

    def test_filter_state(self):
        data = dict(state=self.addresses[0]['geoip']['region'])
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(12, response.data['count'])
        for result in response.data['results']:
            self.assertEqual(result['user']['geoip']['region'], data['state'])

    def test_filter_timestamp(self):
        precise = datetime.datetime(2000, 1, 1, 6, 15, tzinfo=UTC)
        data = dict(timestamp_0=precise.isoformat(),
                    timestamp_1=precise.isoformat())
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(1, response.data['count'])
        for result in response.data['results']:
            timestamp = self.assertTimestamp(result['timestamp'])
            self.assertEqual(timestamp, precise)

    def test_filter_timestamp_multiple(self):
        precise = datetime.datetime(2015, 4, 3, 2, 1, 0, 100000, UTC)
        data = dict(timestamp_0=precise.isoformat(),
                    timestamp_1=precise.isoformat())
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(2, response.data['count'])
        for result in response.data['results']:
            timestamp = self.assertTimestamp(result['timestamp'])
            self.assertEqual(timestamp, precise)

    def test_filter_timestamp_range(self):
        start = datetime.datetime(2000, 1, 1, 0, 12, tzinfo=UTC)
        end = datetime.datetime(2000, 1, 1, 0, 13, tzinfo=UTC)
        data = dict(timestamp_0=start.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                    timestamp_1=end.strftime('%Y-%m-%dT%H:%M:%S.%f'))
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(2, response.data['count'])
        no_z_data = response.data
        data['timestamp_0'] += 'Z'
        data['timestamp_1'] += 'Z'
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        # The "next" link is different.
        no_z_data['next'] = response.data['next']
        self.assertDictEqual(no_z_data, response.data)
        for result in response.data['results']:
            timestamp = self.assertTimestamp(result['timestamp'])
            self.assertGreaterEqual(timestamp, start)
            self.assertLessEqual(timestamp, end)

    def test_filter_timestamp_not_before(self):
        start = datetime.datetime(2001, 1, 1, tzinfo=UTC)
        data = dict(timestamp_0=start.isoformat())
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(8, response.data['count'])
        for result in response.data['results']:
            timestamp = self.assertTimestamp(result['timestamp'])
            self.assertGreaterEqual(timestamp, start)

    def test_filter_timestamp_invalid_format(self):
        data = dict(timestamp_0='invalid datetime format')
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_filter_username_and_timestamp_not_after(self):
        end = datetime.datetime(2001, 1, 1, tzinfo=UTC)
        data = dict(username=self.users[0]['name'],
                    timestamp_1=end.isoformat())
        response = self.client.get(self.path, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code,
                         response.content)
        self.assertEqual(3, response.data['count'])
        for result in response.data['results']:
            self.assertEqual(result['user']['name'], data['username'])
            timestamp = self.assertTimestamp(result['timestamp'])
            self.assertLessEqual(timestamp, end)
