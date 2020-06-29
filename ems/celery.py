import os

from celery import Celery
from django.conf import settings

from .celery_routes import TASK_QUEUES, TASK_ROUTES

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ems.settings")

app = Celery("ems")

app.conf.task_queues = TASK_QUEUES
app.conf.task_routes = TASK_ROUTES

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
