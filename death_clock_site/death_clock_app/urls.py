from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^signup/', signup, name='sign_up'),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^display/', display, name='display'),
    url(r'^index/', index, name='index'),
    url(r'', index, name='index'),
    # catch all for urls so that we go to the index
    url(r'^', RedirectView.as_view(url='/')),

]
