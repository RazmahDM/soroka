"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

activate_this = os.path.expanduser('~/soroka/venv/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

application = get_wsgi_application()
