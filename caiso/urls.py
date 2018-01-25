from django.conf.urls import url

from . import views

urlpatterns = [
    url('yesterdays_mixes', views.yesterdays_mixes),
    url('', views.index),
]
