"""Define URL patterns for users"""
from django.conf.urls import url

from django.contrib.auth import login

from . import views

urlpatterns = [
    #login page
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
]
