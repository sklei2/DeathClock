# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        # otherwise we're going to this page from some redirect
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def index(request):
    user = request.user
    return HttpResponse('{} is all logged in!'.format(user.username))
