"""
Django settings for hackathon_starter project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'keuhh=0*%do-ayvy*m2k=vss*$7)j8q!@u0+d^na7mi2(^!l!d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['django2-hackathon-starter.herokuapp.com', '*']
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'hackathon',
    'bootstrapform',
    # 'django_openid',
    'django_nose',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'api',

    'hijack',
    'hijack_admin',
    'debug_toolbar',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'hackathon_starter.urls'

WSGI_APPLICATION = 'hackathon_starter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# Extra places for collectstatic to find static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'hackathon', 'templates')
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=hackathon/scripts',
]

CORS_ORIGIN_ALLOW_ALL = True

############
#   KEYS   #
############

GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', '')
GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', '')

TUMBLR_CONSUMER_KEY = ''
TUMBLR_CONSUMER_SECRET = ''

INSTAGRAM_CLIENT_ID = ''
INSTAGRAM_CLIENT_SECRET = ''

GOOGLEMAP_API_KEY = os.environ.get('GOOGLEMAP_API_KEY', '')
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''
YAHOO_APP_ID = ''

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

MEETUP_CONSUMER_KEY = ''
MEETUP_CONSUMER_SECRET = ''

BITBUCKET_CONSUMER_KEY = ''
BITBUCKET_CONSUMER_SECRET = ''

LINKEDIN_CLIENT_ID = ''
LINKEDIN_CLIENT_SECRET = ''

YELP_CONSUMER_KEY = ''
YELP_CONSUMER_SECRET = ''
YELP_TOKEN = ''
YELP_TOKEN_SECRET = ''

POPAPIKEY = ''
TOPAPIKEY = ''

QUANDLAPIKEY = ''

FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''

GOOGLE_PLUS_APP_ID = ''
GOOGLE_PLUS_APP_SECRET = ''

DROPBOX_APP_ID = ''
DROPBOX_APP_SECRET = ''

FOURSQUARE_APP_ID = ''
FOURSQUARE_APP_SECRET = ''

# admin changes using the grappelli skin
GRAPPELLI_ADMIN_TITLE = 'Hackathon Starter'
GRAPPELLI_SWITCH_USER = True

HIJACK_USE_BOOTSTRAP = True
HIJACK_ALLOW_GET_REQUESTS = True
