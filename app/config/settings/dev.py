from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'
secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

# .secrets/dev.json의 내용을 사용해서
# 아래 DATABASES내용 채우기
DATABASES = secrets['DATABASES']