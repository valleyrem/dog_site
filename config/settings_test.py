"""SQLite settings for running tests locally without a PostgreSQL server.

Usage:
    SECRET_KEY=test DJANGO_SETTINGS_MODULE=config.settings_test \
        python manage.py test woof
"""

import tempfile
from pathlib import Path

from .settings import *  # noqa: F401,F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Manifest storage requires a collectstatic run; tests don't need it.
STORAGES["staticfiles"]["BACKEND"] = (  # noqa: F405
    "django.contrib.staticfiles.storage.StaticFilesStorage"
)

# In-memory cache keeps tests isolated from the on-disk file cache.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Keep test uploads and imagekit results out of the real media directory.
MEDIA_ROOT = Path(tempfile.mkdtemp(prefix="dogsite-test-"))
