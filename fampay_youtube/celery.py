import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay_youtube.settings')

app = Celery('fampay_youtube')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# The background task to fetch the video data will be ran every
# 30 minutes to compensate for the youtube API key quota.
# Change the time period for the background task by modifying
# the crontab parameters. 

app.conf.beat_schedule ={
    'periodic youtube data fetch':{
        'task':'youtube_api.tasks.periodic_task',
        'schedule': crontab(minute='*/30')
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()