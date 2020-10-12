from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'task_2'

urlpatterns = [
               url(r'^create_task/$', views.GetList.as_view(), name='post_list'),
               ]