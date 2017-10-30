# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader

# Create your views here.

class profileView(generic.ListView):
    template_name = 'profile.html'
    context_object_name = 'profile'
    def get_queryset(self):
        return "asdf"



def index(request):
    return HttpResponse('hello')

def profile(request):
    template = loader.get_template('profile.html')

    context = {
        'user' : request.user.profile.user,
        'date of birth' : str(request.user.profile.dob),
        'life expectancy' : str(request.user.profile.life_expectancy)
    }
    print(context)

    return HttpResponse(template.render(context,request));

