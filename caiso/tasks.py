from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .handlers import GenerationMixHandler


@shared_task
def store_yesterdays_genmixes():
    return GenerationMixHandler('CAISO').store_yesterday()
