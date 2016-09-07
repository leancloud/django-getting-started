# coding: utf-8

from django.conf.urls import url
from django.views import static

import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time/?$', views.current_time),
    url(r'^todos/?$', views.TodoView.as_view(), name='todo_list'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
]
