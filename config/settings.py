"""
Django settings

[introduction](https://docs.djangoproject.com/en/dev/topics/settings/)
[documentation](https://docs.djangoproject.com/en/dev/ref/settings/)
"""

import environ
from pathlib import Path

#======PROJECT-SPECIFIC-SETTINGS===============================================
PROJECT_TITLE = "skeleton-django-sqlite-minmal"
#==============================================================================

# Build paths inside the project like this: ROOT_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = ROOT_DIR / 'apps'

env = environ.Env()
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="Cebo23BMtvLwJ0Q_4UZQMRAHlpTEiJjGZDFWI!R")

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# DATABASES
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# postgres:
# POSTGRES_DB = env.str("POSTGRES_DB")
# POSTGRES_USER = env.str("POSTGRES_USER")
# POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
# POSTGRES_HOST = env.str("POSTGRES_HOST")
# POSTGRES_PORT = env.int("POSTGRES_PORT")
# DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
# DATABASES = {"default": env.db("DATABASE_URL", default=DATABASE_URL)}

# sqlite:
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ROOT_DIR / 'database' / 'sqlite.db'}}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# APPS
# -----------------------------------------------------------------------------
LOCAL_APPS = [
    # custom apps
    "apps.users.apps.UsersConfig",
]

DJANGO_APPS = [
    # default django-apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "django_extensions",
    'widget_tweaks',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
# local apps shall override djangos default, so order is important
INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(ROOT_DIR / "templates")],
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


# users
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/" # "users:redirect"
LOGOUT_REDIRECT_URL = "users:login"
# LOGIN_REDIRECT_URL = "/"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "users:login"

# Django Admin URL.
ADMIN_URL = env.str("DJANGO_ADMIN_URL", default="secretadmin-bonhyAsTh/")

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


# localization-----------------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = "en-us"
# german localization: LANGUAGE_CODE = 'de-de'
TIME_ZONE = "UTC"
# german localization: TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# static folder is renamed to assets (see Jacob Kaplan-Moss - Assets in Django without losing your hair form PyCon 2019 : https://www.youtube.com/watch?v=E613X3RBegI)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/assets/'
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(ROOT_DIR / "assets")]


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
         'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'log_database_queries': {
            '()': 'config.logfilters.LogDatabaseQueriesFilter',
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        'requests_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': str(ROOT_DIR / "logs" / "requests.log"),
        },
        'database_queries_file': {
            'level': 'DEBUG',
            'filters': ['log_database_queries'],
            'class': 'logging.FileHandler',
            'filename': str(ROOT_DIR / "logs" / "database_queries.log"),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
            },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['database_queries_file'],
            'propagate': True,
        }
    }
}
# The logging-filter 'log_database_queries' will log to the file, if LOG_DATABASE is True
# Turn it only on in develop
LOG_DATABASE = False


# django-extensions------------------------------------------------------------
# debug-toolbar
def show_toolbar(request):
    return False #True

if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE.insert(4, "debug_toolbar.middleware.DebugToolbarMiddleware")
    # trick to have debug toolbar when developing with docker
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "config.finders.AssetsAppDirectoriesFinder",
]

# jupyter-notebook-------------------------------------------------------------
IPYTHON_ARGUMENTS = ["--debug", "--settings=config.settings"]
NOTEBOOK_ARGUMENTS = [
    "--port", "8890",
    "--ip", "0.0.0.0",
    "--allow-root",
    "--notebook-dir", "notebooks",
    "--no-browser"
]
# to run the notebook with django 3 async set env DJANGO_ALLOW_ASYNC_UNSAFE=true
