"""
Django settings for MyBuddy project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Environ Variables
KHOA_SERVICE_KEY = os.environ.get('DJANGO_KHOA_SERVICE_KEY', None)
KAKAO_REST_APP_KEY = os.environ.get('DJANGO_KAKAO_REST_APP_KEY', None)
KAKAO_JAVASCRIPT_APP_KEY = os.environ.get('DJANGO_KAKAO_JAVASCRIPT_APP_KEY', None)
DATABASE_NAME = os.environ.get('DJANGO_DB_NAME', None)
DATABASE_HOST = os.environ.get('DJANGO_DB_HOST', None)
DATABASE_PORT = os.environ.get('DJANGO_DB_PORT', None)
static_url = os.environ.get('DJANGO_STATIC_URL', None)
secret_key = os.environ.get('DJANGO_SECRET_KEY', None)
if not secret_key:
    raise ValueError('You must have "SECRET_KEY" variable')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_apscheduler',
    'requests',
    'account',
    'dive',
    'location',
    'third_party_api',
    'front_test',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyBuddy.urls'

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

WSGI_APPLICATION = 'MyBuddy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_NAME,
        'PASSWORD': DATABASE_NAME,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

AUTH_USER_MODEL = 'account.User'

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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    'front_test/static/',
]
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = static_url

# RestFramework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# Scheduler 설정
# - jobs 내용을 Project Database 로 생성
# - thread 에서 실행하는 jobs Application 제어
SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}
SCHEDULER_AUTOSTART = True
# APSCHEDULER_DATETIME_FORMAT =  "N j, Y, f:s a"  # Default

# Session Configurations
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%Y-%b-%d %H:%M:%S'
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'format1',
            'when': 'midnight',
            'backupCount': '10',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['file', 'console'],
        },
        'django': {
            'level': 'WARNING',
            'handlers': ['file', 'console'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
    },
}
