import os

from .settings import *
from .settings import BASE_DIR


# Ensure `ALLOWED_HOSTS` is properly set
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]

# Set debug to False for production
DEBUG = False

# Use the SECRET_KEY from environment variables for security
SECRET_KEY = os.environ['SECRET']

# Middleware setup (unchanged)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Azure storage settings
AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME']  # Your Azure Storage account name
AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY']  # Your Azure Storage account key
AZURE_CONTAINER = os.environ['AZURE_MEDIA_CONTAINER']  # The container name you created

# Set up the DATABASES configuration using environment variables


# Ensure that static and media file paths are correctly set up
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'