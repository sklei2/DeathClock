from django.db import models

"""
Questions store only the text of the question its self
answers must be found in the answer's table using a lookup function/statment
"""
class Question(models.Model):
    question = models.CharField(max_length=4096)

    def __str__(self):
        return self.question


"""
Answers store the question they are attached to, their impact amount and link to an impact type (Cause of Death)
"""
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    impact = models.IntegerField()
    impact_type = models.ForeignKey(Cause_Of_Death, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


"""
Cause of death is used by answers to figure out how its impact fits into the algorithm
"""
class Cause_Of_Death(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name