"""
Django settings for hackachieve project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from hackachieve.classes.Environment import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = Environment.getkey('env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kj%%mx99x(&77^1k60oiij3yq*@19luw#-r4b26w4tybu$-zva'

# SECURITY WARNING: don't run with debug turned on in production!

if ENV == "prod":
    DEBUG = False
    API_HOST = 'https://www.thehackachieve.com:8000/'
    HOST_NAME = 'https://www.thehackachieve.com'
else:
    DEBUG = True
    API_HOST = 'http://localhost:8000/'
    HOST_NAME = 'http://hackachieve.local'

# ================================================================= #
#                      TRANSACTIONAL EMAILS
# ================================================================= #

# current_provider = "mailgun"  # options: postmark, sendgrid, mailgun
#
# # Mailgun =========================== #
#
# if current_provider == 'mailgun':
#
#     EMAIL_HOST = 'smtp.mailgun.org'
#     EMAIL_PORT = 587
#     EMAIL_HOST_USER = Environment.getkey('mailgun_login')
#     EMAIL_HOST_PASSWORD = Environment.getkey('mailgun_password')
#     EMAIL_USE_TLS = True
#
#
# # SENDGRID =========================== #
# elif current_provider == 'sendgrid':
#
#     EMAIL_HOST = 'smtp.sendgrid.net'
#     EMAIL_HOST_USER = Environment.getkey('sendgrid_login')
#     EMAIL_HOST_PASSWORD = Environment.getkey('sendgrid_password')
#     EMAIL_PORT = 587
#     EMAIL_USE_TLS = True
#
#
# # POSTMARK =========================== #
# elif current_provider == 'postmark':
#
#     EMAIL_HOST = 'smtp.postmarkapp.com'
#     EMAIL_PORT = 587
#     EMAIL_HOST_USER = Environment.getkey('postmark_login')
#     EMAIL_HOST_PASSWORD = Environment.getkey('postmark_password')
#     EMAIL_USE_TLS = True

# ================================================================= #
#                      CORS & CSRF
# ================================================================= #


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    # '104.248.222.108',
    # 'thehackachieve.com',
    # 'www.thehackachieve.com'
]

# Application definition
CORS_ORIGIN_ALLOW_ALL = True
#
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
#     '127.0.0.1:8000',
#     '104.248.222.108:8000'
# )
#
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
#
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control'
)

CSRF_TRUSTED_ORIGINS = (
    'localhost:8000',
    '127.0.0.1:8000',
    '104.248.222.108:8000',
    'thehackachieve.com:8000',
    'www.thehackachieve.com:8000'
)

INSTALLED_APPS = [
    'corsheaders',
    'apps.users',
    'apps.countries',
    'apps.provinces',
    'apps.cities',
    'apps.boards',
    'apps.tests',
    'apps.logs',
    'apps.cronjobs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_crontab',
]




MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CorsMiddleware should be as high as possible
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hackachieve.urls'

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_PATH = os.path.join(SETTINGS_PATH, 'hackachieve')
LOGS_PATH = os.path.join(SETTINGS_PATH, 'hackachieve/logs')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_PATH
        ],
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

WSGI_APPLICATION = 'hackachieve.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackachieve',
        'USER': 'django-admin',
        'PASSWORD': '32258190',
        'HOST': '127.0.0.1',
        'POST': '3306',
        'OPTIONS': {
            "init_command": 'SET foreign_key_checks = 0; \
                             SET sql_mode=STRICT_TRANS_TABLES;',

        },
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'rm_database',
    #     'USER': 'hackachieveuser2',
    #     'PASSWORD': '1234',
    #     'HOST': 'localhost',
    #     'POST': '3306',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     },
    # }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

PROPERTIES_IMAGES_ROOT = os.path.join(BASE_DIR, "static") + "/images/properties"

# CUSTOM USER
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}

# ================================================================= #
#                      SIMPLE JWT
# ================================================================= #

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    #
    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': settings.SECRET_KEY,
    # 'VERIFYING_KEY': None,
    #
    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    #
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
    #
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# ================================================================= #
#                      DJANGO LOGGER
# ================================================================= #


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOGS_PATH + "/myapp.log"
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'myapp': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
    },
}


# ================================================================= #
#                      CRON JOBS
# ================================================================= #


CRONJOBS = [
    # ('0 9 * * *', 'cronjobs.cron.check_resume_matches','>> {}/cron.log'.format(LOGS_PATH)) #production - everyday at 9am
    # ('0 9 */2 * *', 'cronjobs.cron.check_resume_matches','>> {}/cron.log'.format(LOGS_PATH)) #production - every two days at 9am
    # ('* * * * *', 'cronjobs.cron.check_resume_matches','>> {}/cron.log'.format(LOGS_PATH)) #dev - every minute
]
CRONTAB_COMMAND_SUFFIX = '2>&1'


# ================================================================= #
#                      SSL
# ================================================================= #

# this is for specific env related configuration


print('ENVIROMENT RUNNING ON {}'.format(ENV))

if ENV == "prod":
    # SSL
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
