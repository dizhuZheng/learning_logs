"""Define URL patterns for users"""
from django.conf.urls import url

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #login page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),
]
