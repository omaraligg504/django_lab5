from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bg_tasks.settings')

app = Celery('bg_tasks')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-3-minutes': {
        'task': 'core.tasks.scheduled_task_code',
        'schedule': crontab(minute='*/3'),
    },
}
