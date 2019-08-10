import os
import sys
import environ

TESTIMG = len(sys.argv) > 1 and sys.argv[1] == 'test'

root = environ.Path(__file__) - 3
env = environ.Env(**{'DEBUG': (bool, True), 'ALLOWED_HOSTS': (list, ['*'])})
environ.Env.read_env(root('.env'))

BASE_DIR = root()
WSGI_APPLICATION = 'demo.wsgi.application'
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY', default='dummy')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
STATIC_URL = env('STATIC_URL', default='/static/')
STATIC_ROOT = env('STATIC_ROOT', default=str(root.path('static')))
MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = env('MEDIA_ROOT', default=str(root.path('media')))
DATABASES = {'default': env.db(default='sqlite:///db.sqlite3')}
INTERNAL_IPS = ['127.0.0.1']
LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')
TIME_ZONE = env('TIME_ZONE', default='UTC')
USE_I18N = env('USE_I18N', default=True)
USE_L10N = env('USE_L10N', default=True)
USE_TZ = env('USE_TZ', default=True)
ROOT_URLCONF = 'demo.urls'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=None)
EMAIL_CONFIG = env.email_url('EMAIL_URL', default='consolemail://')
vars().update(EMAIL_CONFIG)
if not TESTIMG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cbvadmin',
    'cbvadmin_semantic_ui',
    'crispy_forms',
    'crispy_forms_semantic_ui',
    'django_tables2',
    'django_filters',
    'menu',
    'app'
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

# Configure debug toolbar
DEBUG_TOOLBAR = env('DEBUG_TOOLBAR', default=DEBUG)
try:
    import debug_toolbar
except ImportError:
    DEBUG_TOOLBAR = False

if DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_COLLAPSED': True
    }
