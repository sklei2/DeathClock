# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .forms import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                auth_login(request, user)
    else:
        # otherwise we're going to this page from some redirect
        form = LoginForm

    return render(request, 'login.html', {'form': form})


@login_required
def index(request):
    user = request.user
    return HttpResponse('{} is all logged in!'.format(user.username))
