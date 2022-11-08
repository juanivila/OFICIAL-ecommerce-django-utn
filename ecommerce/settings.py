import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-n$glc%3-x3#g(1asy9s6j-3+osm&_fj9@xu947-!q^yww_42th'

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
	'django.contrib.sites',
	'registration',  # should be immediately above 'django.contrib.admin'
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	
	# My apps
	'usuarios.apps.UsuariosConfig',
	'productos.apps.ProductosConfig',
	'contacto.apps.ContactoConfig',
	
	# Third party apps
	'debug_toolbar',
	]

MIDDLEWARE = [
	# Third party middleware
	"debug_toolbar.middleware.DebugToolbarMiddleware",
	
	# Django middleware
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	
	]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
		}
	}

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

# Language
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static & Media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = '127.0.0.1'

# Registration Redux
LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = 'django.contrib.auth.views.login'
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.
SITE_ID = 1
