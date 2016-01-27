import os
from django.conf import settings
import dj-database-url

DEBUG= False
TEMPLATE_DEBUG = True
DATABASES=settings.DATABASES
DATABASES['default']=dj-database-url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','http')

ALLOWED_HOSTS = ['*']


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL= '/static/'
# STATICFILES_DIRS = (
    # os.path.join(BASE_DIR,'static')
# )