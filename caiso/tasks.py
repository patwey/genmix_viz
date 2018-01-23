from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .handlers import GenerationMixDataHandler


@shared_task
def store_latest_generation():
    return GenerationMixDataHandler('CAISO').store_latest()
