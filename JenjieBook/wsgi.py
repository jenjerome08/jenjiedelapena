"""
WSGI config for JenjieBook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os
import sys

sys.path.append('path/to/yourprojectenv/lib/python3.8/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JenjieBook.settings')

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

