"""
WSGI config for django_example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_example.settings")

profile = os.environ.get('DJANGO_EXAMPLE_PROF工LE' , 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"django_example.settings.%s" % profile)

application = get_wsgi_application()
