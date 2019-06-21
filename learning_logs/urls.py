"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from .views import index, topics, topic

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),

    # Show all topics.
    url(r'^topics/$', topics, name='topics'),

    #show all topics
    url(r'^topics/(?P<topic_id>\d+)/$', topic, name='topic'),
]
