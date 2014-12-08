# -*- coding: utf-8 -*-
"""
Django settings for LFS Development project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
from os.path import join, dirname
from django.utils.translation import gettext_lazy as _

from configurations import Configuration, values

BASE_DIR = dirname(dirname(__file__))


class Common(Configuration):

    # APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.flatpages',
        'django.contrib.redirects',
        'django.contrib.sitemaps',
        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'lfs_theme',
        'compressor',
        'django_countries',
        'pagination',
        'reviews',
        'portlets',
        'lfs',
        'lfs.addresses',
        'lfs.caching',
        'lfs.cart',
        'lfs.catalog',
        'lfs.checkout',
        'lfs.core',
        'lfs.criteria',
        'lfs.customer',
        'lfs.customer_tax',
        'lfs.discounts',
        'lfs.export',
        'lfs.gross_price',
        'lfs.mail',
        'lfs.manage',
        'lfs.marketing',
        'lfs.manufacturer',
        'lfs.net_price',
        'lfs.order',
        'lfs.page',
        'lfs.payment',
        'lfs.portlet',
        'lfs.search',
        'lfs.shipping',
        'lfs.supplier',
        'lfs.tax',
        'lfs.tests',
        'lfs.utils',
        'lfs.voucher',
        'lfs_contact',
        'lfs_order_numbers',
        'localflavor',
        'postal',
        'paypal.standard.ipn',
        'south',
        'lfs_criterion_us_states',
        'django_nose',
        'debug_toolbar',
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        # Your stuff: custom apps go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
    # END APP CONFIGURATION

    # MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
        "pagination.middleware.PaginationMiddleware",
        "lfs.utils.middleware.AJAXSimpleExceptionResponse",
        "lfs.utils.middleware.ProfileMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # MIGRATIONS CONFIGURATION
    # MIGRATION_MODULES = {
    #     'sites': 'contrib.sites.migrations'
    # }
    # END MIGRATIONS CONFIGURATION

    # DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = "CHANGEME!!!"
    # END SECRET CONFIGURATION

    # FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    # END FIXTURE CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        # ('Your Name', 'your_email@domain.com'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    # DATABASES = values.DatabaseURLValue('postgres://localhost/lfs')
    DATABASES = values.DatabaseURLValue('sqlite:///lfs.db')
    # END DATABASE CONFIGURATION

    # CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify (used on heroku) is painful to install on windows.
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }
    # END CACHING

    # GENERAL CONFIGURATION
    SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'UTC'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    # END GENERAL CONFIGURATION

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.debug',
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'lfs.core.context_processors.main',
        # Your stuff: custom template context processors go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'sitestatic')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    # STATICFILES_DIRS = (
    #     join(BASE_DIR, 'static'),
    # )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        # 'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = 'urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        'lfs.customer.auth.EmailBackend',
        "django.contrib.auth.backends.ModelBackend",
    )

    # Auth defaults
    LOGIN_REDIRECT_URL = "/manage/"
    LOGIN_URL = "/login/"
    # END Auth defaults

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        "version": 1,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s %(levelname)s %(message)s",
                "datefmt": "%a, %d %b %Y %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
            'logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': os.path.join(BASE_DIR, "..", "lfs.log"),
                'mode': 'a',
            },
        },
        "loggers": {
            "default": {
                "handlers": ["logfile", "console"],
                "level": "DEBUG",
                "propagate": False,
            },
        }
    }
    # END LOGGING CONFIGURATION

    # COMPRESS CONFIGURATION
    COMPRESS_ENABLED = False
    COMPRESS_CACHE_BACKEND = 'locmem:///'
    # END COMPRESS CONFIGURATION

    # LFS CONFIGURATION
    PAYPAL_RECEIVER_EMAIL = "info@yourbusiness.com"
    PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

    LFS_PAYPAL_REDIRECT = True
    LFS_AFTER_ADD_TO_CART = "lfs_added_to_cart"
    LFS_RECENT_PRODUCTS_LIMIT = 5

    LFS_LOCALE = "en_US.UTF-8"

    LFS_ORDER_NUMBER_GENERATOR = "lfs_order_numbers.models.OrderNumberGenerator"
    LFS_DOCS = "http://docs.getlfs.com/en/latest/"

    LFS_INVOICE_COMPANY_NAME_REQUIRED = False
    LFS_INVOICE_EMAIL_REQUIRED = True
    LFS_INVOICE_PHONE_REQUIRED = True

    LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
    LFS_SHIPPING_EMAIL_REQUIRED = False
    LFS_SHIPPING_PHONE_REQUIRED = False

    LFS_PAYMENT_METHOD_PROCESSORS = [
        ["lfs_paypal.PayPalProcessor", _(u"PayPal")],
    ]

    LFS_PRICE_CALCULATORS = [
        ['lfs.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
        ['lfs.net_price.NetPriceCalculator', _(u'Price excludes tax')],
    ]

    LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
        ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
        ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
    ]

    LFS_UNITS = [
        u"l",
        u"m",
        u"qm",
        u"cm",
        u"lfm",
        u"Package",
        u"Piece",
    ]

    LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

    LFS_CRITERIA = [
        ["lfs.criteria.models.CartPriceCriterion", _(u"Cart Price")],
        ["lfs.criteria.models.CombinedLengthAndGirthCriterion", _(u"Combined Length and Girth")],
        ["lfs.criteria.models.CountryCriterion", _(u"Country")],
        ["lfs.criteria.models.HeightCriterion", _(u"Height")],
        ["lfs.criteria.models.LengthCriterion", _(u"Length")],
        ["lfs.criteria.models.WidthCriterion", _(u"Width")],
        ["lfs.criteria.models.WeightCriterion", _(u"Weight")],
        ["lfs.criteria.models.ShippingMethodCriterion", _(u"Shipping Method")],
        ["lfs.criteria.models.PaymentMethodCriterion", _(u"Payment Method")],
        ["lfs_criterion_us_states.models.USStatesCriterion", _(u"US State")],
    ]

    REVIEWS_SHOW_PREVIEW = False
    REVIEWS_IS_NAME_REQUIRED = False
    REVIEWS_IS_EMAIL_REQUIRED = False
    REVIEWS_IS_MODERATED = False
    # END LFS CONFIGURATION

    # JENKINS CONFIGURATION
    # apps that we want jenkins ci to test
    PROJECT_APPS = ['lfs.core']
    JENKINS_TASKS = (
        'django_jenkins.tasks.run_pylint',
        #'django_jenkins.tasks.with_coverage',
        'django_jenkins.tasks.django_tests',
        'django_jenkins.tasks.run_pep8',
        'django_jenkins.tasks.run_pyflakes',
        #'django_jenkins.tasks.windmill_tests',
    )
    # END JENKINS CONFIGURATION

    PISTON_DISPLAY_ERRORS = True

    # disable south logger while running tests to prevent output of huge amount of data
    if 'test' in sys.argv:
        LOGGING['loggers']['south'] = dict(level="INFO")


    # Your common stuff: Below this line define 3rd party library settings