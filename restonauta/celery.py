import os
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restonauta.settings')

app = Celery('restonauta')

app.conf.broker_url = 'amqp://localhost'
app.conf.result_backend = 'rpc://'

# Configuración opcional
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.worker_prefetch_multiplier = 1

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')