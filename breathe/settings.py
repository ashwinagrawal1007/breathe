DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dr.sqlite3',
    },
}

INSTALLED_APPS = (
    
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.admin',
    'registration',
    'breathe',
    'bootstrapform',
)


DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = '_'

SITE_ID = 1

ROOT_URLCONF = 'breathe.urls_default'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Breathe Registration]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'


from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger',}

LOGIN_REDIRECT_URL = '/console'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sensorcloud',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'sjsu',
            'PASSWORD': 'sanjosesjsu',
            'HOST': 'sensorcloudproject.cjbwwgkhqpwt.us-west-2.rds.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }