# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
user_obj.UserInf
"""
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1,
                           choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female')
                                    ),
                           null=True)

"""
Hook up our extra information so that when we make a user we can have
these fields.
"""
@receiver(post_save, sender=User)
def create_user_prifle(sender, instance, created, **kwargs):
    if created:
        DeathStats.objects.create(user=instance)
        UserInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.deathStats.save()
    instance.userInfo.save()
