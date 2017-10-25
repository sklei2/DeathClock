
from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    url(r'^login/', login),
    url(r'', index),
    # catch all for urls so that we go to the index
    url(r'^', RedirectView.as_view(url='/')),
]
