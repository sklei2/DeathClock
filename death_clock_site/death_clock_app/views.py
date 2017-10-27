# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import DummyForm

# Create your views here.

def dummyForm(request):
    if request.method == 'POST':
        form = DummyForm(request.POST)
        if form.is_valid():
            return HttpResponse('hi')
    else:
        form = DummyForm()
    return render(request, 'dummy.html', {'form': form})

def index(request):
    return HttpResponse('hello')


