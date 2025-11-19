from pathlib import Path

from config.env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env.read_env(BASE_DIR / '.env')


SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.str('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# APPS
SHARED_APPS = [
    'django_tenants',
    'jazzmin',
    'core.apps.customers',
    'django.contrib.contenttypes',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TENANT_APPS = [
    'core.apps.shared',
]

PACKAGES = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
]


INSTALLED_APPS = SHARED_APPS + DJANGO_APPS + PACKAGES + TENANT_APPS

# Middlewares
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]


LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Media and Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'resources/static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'resources/media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django tenants
TENANT_MODEL = "customers.Client" 

TENANT_DOMAIN_MODEL = "customers.Domain"


import config.conf 