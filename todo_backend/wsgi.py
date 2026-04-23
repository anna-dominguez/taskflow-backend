"""
WSGI config for todo_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sentry_sdk

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_backend.settings.development')

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    traces_sample_rate=1.0,
    environment=os.environ.get('DJANGO_ENV', 'development'),
)

application = get_wsgi_application()
