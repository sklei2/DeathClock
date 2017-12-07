from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Questions store only the text of the question its self
answers must be found in the answer's table using a lookup function/statment
"""
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=4096)

    def __str__(self):
        return self.question


"""
Cause of death is used by answers to figure out how its impact fits into the algorithm
"""
class CauseOfDeath(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

"""
Symptoms are linked to answers, can be solid value or multiplier
"""
class Symptom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1024)
    impact = models.IntegerField()
    multiplier = models.BooleanField()
    cause = models.ForeignKey(CauseOfDeath, on_delete=models.CASCADE)

"""
Mapper table between answers and symptoms (many to many)
"""
class QuestionSymptomMapper(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)





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
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1,
                           choices=(
                               ('M', 'Male'),
                               ('F', 'Female')
                           ),
                           null=True)
    life_expectancy = models.DateTimeField(null=True)


"""
Hook up our extra information so that when we make a user we can have
these fields.
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
