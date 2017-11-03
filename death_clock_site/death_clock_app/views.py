# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader

import datetime

# Create your views here.

def profile(request):
    template = loader.get_template('profile.html')

    today = datetime.date.today()
    temp = request.user.profile.life_expectancy
    request.user.profile.life_expectancy = temp - today

    return render(request, 'profile.html' )

