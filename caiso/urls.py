from django.conf.urls import url

from . import views

urlpatterns = [
    url('latest', views.latest_generation_day)
]
