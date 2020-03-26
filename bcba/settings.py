"""
Django settings for bcba project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['bcba-v1.herokuapp.com', 'www.orizaba.co.uk', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_websites',
    'app_admins',
    'app_contacts',
    'app_users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Comment this out when working locally. Uncomment when deploying to show static files.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bcba.urls'

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

WSGI_APPLICATION = 'bcba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

### Comment out one of the below databases ###

# Uses the LIVE DB Locally
DATABASES = {
   'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
   }
}

# This below only relates to local development and can be commented out when pushing to production.
DATABASES['default'] = dj_database_url.config(default='postgres://xurczkuelkilmc:24d098180170ce6662cceaa636fc5ad003c32b6e9c43ddb535fb05bf6e298fa8@ec2-3-211-48-92.compute-1.amazonaws.com:5432/d5qvb86an33ckb')

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Uses the LOCAL DB Locally
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'bcba',
#        'USER': 'postgres',
#        'PASSWORD': 'Theturtle1$',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
        ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

# Media Files # 

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Sendgrid Settings

SEND_GRID_API_KEY = config('SENDGRID_KEY')
SECRET_KEY = config('SECRET_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'ben_taylor'
EMAIL_HOST_PASSWORD = 'Theturtle1$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ben@gardentractorspares.co.uk'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact Email Message'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
