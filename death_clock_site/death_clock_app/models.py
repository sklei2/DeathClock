# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


"""
Extending the User model so that we can store information
related to them in this class. 
"""
class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

