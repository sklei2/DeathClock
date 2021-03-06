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
from .models import *
from . import death_algorithm
from django.template import loader
import datetime


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
                form.register()
                return HttpResponseRedirect(reverse('login'))
            except IntegrityError:
                # We already have this user!
                render(request, 'signup.html', {'form': form,
                                                'message': 'user already exists'})
    else:
        form = UserSignupForm
    return render(request, 'signup.html', {'form': form})


def profile(request):
    template = loader.get_template('profile.html')

    try:
        today = datetime.date.today()
        life_expectancy = request.user.profile.life_expectancy - today
    except TypeError:
        life_expectancy = "Please take our test first"

    return render(request, 'profile.html', {'life_expectancy': life_expectancy})


@login_required(login_url='/login/')
def index(request):
    user = request.user
    # If post, then display form with previous data
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        # Insert code to apply results to user object here

        # Filter POST Data to get all questions
        questions = []
        for item in request.POST:
            if str(item) != "csrfmiddlewaretoken":
                questions.append(item)

        #send questions to algorithm
        user_profile = Profile.objects.get(user=user)
        years_to_live = death_algorithm.run_algorithm(questions, user_profile)
        # convert life expectancy to ms so that we can add it to our DOB
        ms_to_live = years_to_live * 365 * 24 * 60 * 60 * 1000
        user_profile.life_expectancy = user_profile.dob + datetime.timedelta(milliseconds=ms_to_live)
        user_profile.save()
        user.save()
        # go to the display page
        return HttpResponseRedirect(reverse('display'))
    else:
        # If get, then display new form
        form = QuestionForm()

    return render(request, 'index.html', {'username': user.username, 'form': form})


def display(request):
    profile = Profile.objects.get(user=request.user)
    if profile.life_expectancy:
        return render(request, 'display.html', {'life_expectancy': profile.life_expectancy})
    else:
        return render(request, 'display.html', {})
