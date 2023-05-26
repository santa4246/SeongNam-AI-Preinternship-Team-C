"""
Django settings for backend project.

Generated by 'backend-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'foo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 1))

if os.getenv('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'backend']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'chat_teesis.apps.ChatTeesisConfig',
    'corsheaders',
    'drf_yasg',
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'eg_user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'eg_pw'),
        'HOST': os.environ.get('SQL_HOST', 'eg_db'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

RABBITMQ_HOSTS = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_QUEUE_EXPIRES = 300.0
RABBITMQ_MESSAGE_EXPIRES = RABBITMQ_QUEUE_EXPIRES

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'backend.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CORS realted settings

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_METHODS = ['DELETE','GET','OPTIONS','PATCH','POST','PUT']

CORS_ORIGIN_WHITELIST = ['http://localhost:8000',
                         'http://localhost:8081',
                         'http://localhost:9090',
                         'http://localhost:5432',
                         'http://localhost:5672',
                         'http://localhost:15672',
                         'http://localhost:80',
                         'http://localhost']

CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
