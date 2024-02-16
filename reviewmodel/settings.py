"""
Django settings for reviewmodel project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# setting updated by admin

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6+er01pco09=&q&9@ipv8j7y#2mj-s6zjq$dpf45n-(gtzk$u1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'
    # '127.0.0.1'
    # '420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev',
    # # "http://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/",
    # # "http://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/5/",
    # # "http://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/4/",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp2',
    'Reviews',
    "crispy_forms",
    'corsheaders',
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_COOKIE_SECURE = True  # Set to False for development with HTTP
CSRF_COOKIE_HTTPONLY = True

CSRF_TRUSTED_ORIGINS = [
    'https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev',
]

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + ("custom-headers", )

CORS_ALLOWED_ORIGINS = [
    # "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/",
    # "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/5",
    # "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/4",
    # Add more allowed origins if needed
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "https://Your frontend host",
    "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/",
    "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/5/",
    "https://420bd50a-19fd-41a2-b6eb-9827fe8d8dc1-00-kcz7kls9lyrn.spock.replit.dev/properties/4/",
)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'reviewmodel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
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

WSGI_APPLICATION = 'reviewmodel.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mshariq28022000@gmail.com'
EMAIL_HOST_PASSWORD = 'usir bluw tvai xzyb'


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR,
    "static",
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
