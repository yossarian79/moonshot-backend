import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Question.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

try:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
except:
    pass    