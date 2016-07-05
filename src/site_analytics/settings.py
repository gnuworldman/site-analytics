"""Django settings for site_analytics project."""

import os


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'site_analytics.apps.SiteAnalyticsAppConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'site_analytics.urls'

SECRET_KEY = '1l8=#(x54(wg=y-=z*d@5mz*13wljew4_0dwq2#a7b$$539q!='

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'site_analytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'site_analytics',
        'USERNAME': 'site_analytics',
        'PASSWORD': 'yD8L1qS3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

pv_module = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': pv_module + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': pv_module + '.MinimumLengthValidator',
    },
    {
        'NAME': pv_module + '.CommonPasswordValidator',
    },
    {
        'NAME': pv_module + '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = 'UTC'
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

project_package_dir = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(project_package_dir, 'static_root')
STATIC_URL = '/static/'


# Django REST Framework
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.DjangoFilterBackend',
    ],
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    # Disable the Browsable API by default; enable in settings_local.py with:
    #   from .settings import REST_FRAMEWORK
    #   REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
    #       'rest_framework.renderers.BrowsableAPIRenderer')
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'URL_FIELD_NAME': 'self',
}


# Optionally load any local settings.
try:
    from .settings_local import *  # noqa
except ImportError as exc:  # pragma: nocover
    if exc.name != __package__ + '.settings_local':
        raise
