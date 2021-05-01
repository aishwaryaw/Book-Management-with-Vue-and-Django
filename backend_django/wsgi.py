"""
WSGI config for backend_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loading the .env file
dotenv_file = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_file)

application = get_wsgi_application()
