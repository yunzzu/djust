
from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file = os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False       #개발중인 상태

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #mysql을 써서 mariadb와 연동시킴
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret('MYSQL_ROOT_HOST'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}