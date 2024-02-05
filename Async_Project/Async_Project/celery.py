from __future__ import absoulute_import,unicode_literals
import os  
from celery import Celery  



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasker.settings')

app = Celery('tasker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()