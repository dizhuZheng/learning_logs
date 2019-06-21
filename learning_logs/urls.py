"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from .views import index, topics

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),

    #show all topics
    url(r'^topics/$', topics, name='topics'),
]
