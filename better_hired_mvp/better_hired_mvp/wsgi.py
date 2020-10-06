"""
WSGI config for better_hired_mvp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better_hired_mvp.better_hired_mvp.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better_hired_mvp.settings')

application = get_wsgi_application() 