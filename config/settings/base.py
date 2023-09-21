"""
Django settings for parvoz_turizm project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ye834nv)m2_lu+w0+iy05^d-*peq&ii99mk%n56i-2gz0kadqu'


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    'rest_framework_jwt',
    'modeltranslation',
    "corsheaders",
    "rest_framework_swagger",
    'django_filters',
    'debug_toolbar',
]

LOCAL_APPS = [
    "main.apps.account.apps.AccountConfig",
    "main.apps.client.apps.ClientConfig",
    "main.apps.hotel.apps.HotelConfig",
    "main.apps.outfit.apps.OutfitConfig",
    "main.apps.expense.apps.ExpenseConfig",
    "main.apps.package.apps.PackageConfig",
    "main.apps.transport.apps.TransportConfig",
    "main.apps.flight.apps.FlightConfig",
    "main.apps.visa.apps.VisaConfig",
    "main.apps.employee.apps.EmployeeConfig"
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'
os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-root'

AUTH_USER_MODEL = 'account.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
       'rest_framework_simplejwt.authentication.JWTAuthentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
    ),
    # "DEFAULT_PAGINATION_CLASS": "main.apps.common.pagination.PageNumberPagination",
    # "PAGE_SIZE": 12,
    # "DEFAULT_FILTER_BACKENDS": (
    #     "django_filters.rest_framework.DjangoFilterBackend",
    #     "rest_framework.filters.SearchFilter",
    # ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",

    "DATA_UPLOAD_MAX_MEMORY_SIZE": 100 * 1024 * 1024,
    "FILE_UPLOAD_MAX_MEMORY_SIZE": 100 * 1024 * 1024,

    "DEFAULT_TIMEOUT":300
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
       "default": {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("POSTGRES_HOST"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "PORT": os.environ.get("POSTGRES_PORT"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

gettext = lambda s: s
LANGUAGES = (
    ('uz', gettext('Uzbek')),
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "main", "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "main", "static/")


CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CSRF_TRUSTED_ORIGINS = [
    "https://abdullaevdev.uz",
    "http://66.55.68.250",
    'http://localhost:5173',
    'http://localhost:3000',
    "http://127.0.0.1:8000",
]

CORS_ALLOWED_ORIGINS = [
    "https://abdullaevdev.uz",
    "https://parvoz.site.uz",
    "http://66.55.68.250",
    'http://localhost:5173',
    'http://localhost:3000',
    "http://127.0.0.1:8000",
]


OWNER = "owner"
MODERATOR = "moderator"
SALESMAN = "salesman"


DIRECT_FLIGHT = "direct_flight"
CHARTERED_FLIGHT = "chartered_flight"

