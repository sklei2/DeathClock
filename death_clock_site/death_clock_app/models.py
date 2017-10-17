# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


"""
Storing extra information in the User model for their 
death information. This is information we'd get AFTER they
complete the survey

To access this information we grab the user object then go
user_obj.DeathStats
"""
class DeathStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # date we think the user will live until
    life_expectancy = models.DateField()


"""
Storing extra informatino in the User model for their
general information. This is something that we could possibly
get when we first create the profile.

To access this information we grab the user object then go
user_obj.UserInfo
"""
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=(
                                                   ('M', 'Male'),
                                                   ('F','Female')
                                                 ))
