# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Storing extra information in the User model for their
general information. This is something that we could possibly
get when we first create the profile.

To access this information we grab the user object then go
user_obj.UserInf
"""


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=(
                                                   ('M', 'Male'),
                                                   ('F', 'Female')
                                                 ))
    life_expectancy = models.DateField(null=True)

    class Meta:
        db_table = 'user_info'


"""
Hook up our extra information so that when we make a user we can have
these fields.
"""


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
