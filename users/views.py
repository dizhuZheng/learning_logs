from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.

def logout_view(request):
    """log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
