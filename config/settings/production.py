# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''
from __future__ import absolute_import, unicode_literals

from .common import *  # noga

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
)

# EMAIL
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='LFS Development <noreply@getlfs.com>')
EMAIL_HOST = env('DJANGO_EMAIL_HOST', default='smtp.sendgrid.com')
EMAIL_HOST_USER = env('EMAIL_USERNAME')
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[LFS Development] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL")

# CACHING
# ------------------------------------------------------------------------------
try:
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify is painful to install on windows.
    # See: https://github.com/rdegges/django-heroku-memcacheify
    from memcacheify import memcacheify
    CACHES = memcacheify()
except ImportError:
    CACHES = {
        'default': env.cache_url("DJANGO_CACHE_URL", default="memcache://127.0.0.1:11211"),
    }

# Your production stuff: Below this line define 3rd party libary settings