from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .adapters import GenerationAdapter


@shared_task
def store_latest_generation():
    return GenerationMixHandler('CAISO').store_latest()
