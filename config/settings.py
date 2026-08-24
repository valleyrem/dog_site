"""
Django settings for the woofdogs.world project.

All sensitive values come from environment variables (see django-environ).
A `.env` file in the project root is read automatically.
"""

import os
from pathlib import Path

import environ
from botocore.config import Config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read the environment file from config/.env (explicit path: read_env()
# without arguments looks next to manage.py in the project root).
env = environ.Env()
environ.Env.read_env(BASE_DIR / "config" / ".env")


# Security
# https://docs.djangoproject.com/en/5.1/ref/settings/#security

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=["https://woofdogs.world", "https://dev.woofdogs.world"],
)

# Enable when running behind an HTTPS reverse proxy (nginx, traefik, caddy).
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Applications

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "woof.apps.WoofConfig",
    "smart_selects",
    "imagekit",
    # local-only tooling
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", default="dog_site"),
        "USER": env("DATABASE_USER", default="dog_site"),
        "PASSWORD": env("DATABASE_PASS", default=""),
        "HOST": env("DB_HOST", default="127.0.0.1"),
        "PORT": env("DB_PORT", default="5432"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "Europe/Belgrade"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"

# Source directories for static files: project-level assets (static/)
# and app assets (woof/static/, picked up by the AppDirectoriesFinder).
# STATIC_ROOT is where `collectstatic` gathers them for deployment.
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Manifest storage adds content hashes to file names and requires
# `collectstatic` to be run (done in the Docker build). In DEBUG mode we fall
# back to plain storage so the development server works out of the box.
if DEBUG:
    _STATIC_BACKEND = "whitenoise.storage.CompressedStaticFilesStorage"
else:
    _STATIC_BACKEND = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (user uploads)
# https://docs.djangoproject.com/en/5.1/topics/files/
#
# With USE_S3=True files go to an S3-compatible bucket (OCI Object
# Storage); otherwise the local filesystem is used.
USE_S3 = env.bool("USE_S3", default=False)

if USE_S3:
    _DEFAULT_STORAGE = {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": env("S3_ACCESS_KEY_ID"),
            "secret_key": env("S3_SECRET_ACCESS_KEY"),
            "bucket_name": env("S3_BUCKET_NAME"),
            "region_name": env("S3_REGION", default="eu-milan-1"),
            "endpoint_url": env("S3_ENDPOINT_URL"),
            "default_acl": "public-read",
            "file_overwrite": False,
            # Public bucket: serve plain permanent URLs instead of
            # pre-signed ones (which expire after an hour).
            "querystring_auth": False,
            "url_protocol": "https:",
            # OCI Object Storage does not support AWS chunked payloads
            # (botocore >= 1.36 enables them by default); use unsigned
            # payloads over HTTPS instead.
            "client_config": Config(
                signature_version="s3v4",
                # botocore >= 1.36 defaults to CRC32 checksums on every Put,
                # which forces aws-chunked encoding; OCI does not support it.
                request_checksum_calculation="when_required",
            ),
        },
    }
else:
    _DEFAULT_STORAGE = {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }

STORAGES = {
    "default": _DEFAULT_STORAGE,
    "staticfiles": {
        "BACKEND": _STATIC_BACKEND,
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Cache
# https://docs.djangoproject.com/en/5.1/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# django-debug-toolbar (active only with DEBUG=True and local IPs)

INTERNAL_IPS = [
    "127.0.0.1",
]


# Telegram bot for the contact form

TELEGRAM_BOT_TOKEN = env("TOKEN", default="")
TELEGRAM_CHAT_ID = env("CHAT_ID", default="")
