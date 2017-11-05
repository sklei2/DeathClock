# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .forms import *
from django.db import IntegrityError
from django.urls import reverse
from . import death_algorithm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=user_name, password=password)
            if user is not None and user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        # otherwise we're going to this page from some redirect
        form = LoginForm

    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            try:
                user_name = request.POST.get('username')
                pwd = request.POST.get('pwd')
                user = User.objects.create_user(username=user_name, password=pwd)
                user.save()
                return HttpResponseRedirect(reverse('login'))
            except IntegrityError:
                # We already have this user!
                render(request, 'signup.html', {'form': form,
                                                'message': 'user already exists'})
    else:
        form = UserSignupForm
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login/')
def index(request):
    user = request.user

    # If post, then display form with previous data
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        # Insert code to apply results to user object here
        death_algorithm([x for x in request.POST if x.key != 'csrfmiddlewaretoken'])

    # If get, then display new form
    else:
        form = QuestionForm()

    return render(request, 'index.html', {'username': user.username, 'form': form})
