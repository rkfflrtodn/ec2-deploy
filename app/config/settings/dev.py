from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True
ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

WSGI_APPLICATION = 'config.wsgi.dev.application'

# .secrets/dev.json의 내용을 사용해서
# 아래 DATABASES설정 채우기
DATABASES = secrets['DATABASES']

# django-storages
# ~/.aws/credentials
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# collectstatic을 실행했을 때,
# 버킷의 'static'폴더 아래에 정적파일들이 저장되도록 설정해보기
#  config.storages.StaticStorage클래스를 만들어서 적용
# STATICFILES_STORAGE = 'config.storages.StaticStorage'
# 위 설정시 S3 프리티어의 기본 PUT한계를 금방 초과하게되므로
#  STATIC_ROOT에 collectstatic후 Nginx에서 제공하는 형태로 사용
AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# 로그폴더 생성
LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s'
        },
    },
    'handlers': {
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'file_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file_error', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

DEBUG = False
ALLOWED_HOSTS = ['abc']