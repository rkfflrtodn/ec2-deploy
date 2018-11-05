from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

# .secrets/dev.json의 내용을 사용해서
# 아래 DATABASES설정 채우기
DATABASES = secrets['DATABASES']

# django-storages
# ~/.aws/credentials
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# collectstatic을 실행했을 때,
# 버킷의 'static'폴더 아래에 정적파일들이 저장되도록 설정해보기
#  config.storages.StaticStorage클래스를 만들어서 적용
AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']