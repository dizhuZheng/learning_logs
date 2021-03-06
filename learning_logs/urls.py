"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from .views import index, topics, topic, new_topic, new_entry, edit_entry, edit_topic

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),

    # Show all topics.
    url(r'^topics/$', topics, name='topics'),

    #show all topics
    url(r'^topics/(?P<topic_id>\d+)/$', topic, name='topic'),

    #page for adding a new topic
    url(r'^new_topics/$', new_topic, name='new_topic'),

    url(r'^new_entry/(?P<topic_id>\d+)/$', new_entry, name='new_entry'),

    #page for editing an entry
    url(r'^edit_entry/(?P<edit_id>\d+)/$', edit_entry, name='edit_entry'),

    #page for editing a topic
    url(r'^edit_topic/(?P<edit_id>\d+)/$', edit_topic, name='edit_topic')
]
