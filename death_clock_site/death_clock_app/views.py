# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .forms import *



# Create your views here.
def index(request):
	# If post, then display form with previous data
	if request.method == 'POST':
		form = QuestionForm(data=request.POST)
		# Insert code to apply results to user object here

	# If get, then display new form
	else:
		form = QuestionForm()

	return render(request, 'index.html', {'form': form})
