from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Resposta


@shared_task
def task_votar(resposta_pk):
    Resposta.votar(resposta_pk)
