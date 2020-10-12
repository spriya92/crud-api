from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'crud'

urlpatterns = [
               url(r'^postservice/$', views.GetList.as_view(), name='post_list'),
               url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view()),
               ]