"""
WSGI config for home_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home_site.settings")

application = get_wsgi_application()

# Heroku deployment
ON_HEROKU = 'ON_HEROKU' in os.environ

if ON_HEROKU:
    application = DjangoWhiteNoise(application)
