
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'unsafe'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
 'django.contrib.contenttypes','django.contrib.auth',
 'django.contrib.sessions','django.contrib.messages',
 'django.contrib.staticfiles','rest_framework',
 'customers','loans'
]

DATABASES = {
 'default': {
  'ENGINE':'django.db.backends.postgresql',
  'NAME':'creditdb','USER':'postgres','PASSWORD':'postgres','HOST':'db','PORT':5432
 }
}

ROOT_URLCONF = 'credit_system.urls'
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
