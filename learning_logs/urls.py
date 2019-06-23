"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from .views import index, topics, topic, new_topic, new_entry

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),

    # Show all topics.
    url(r'^topics/$', topics, name='topics'),

    #show all topics
    url(r'^topics/(?P<topic_id>\d+)/$', topic, name='topic'),

    #page for adding a new topic
    url(r'^new_topics/$', new_topic, name='new_topic'),

    url(r'^new_entry/(?P<topic_id>\d+)/$', new_entry, name='new_entry')
]
