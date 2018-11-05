from .base import *
secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))
DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}