from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import *

# Question object for easy storage of form questions
class QuestionObj:
	text = ''
	answers = []
	def __init__(self, q, a):
		self.text = q
		self.answers = a

# Given a question, returns all answers for the question
def GetQuestions(q):
	answerList = []
	index = 0
	for ans in Answer.objects.filter(question=q):
		answerList.append((index, ans.text))
		index += 1
	return answerList

# Question form
class QuestionForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)

		for q in Question.objects.all():
			tempq = QuestionObj(q.question, GetQuestions(q))
			self.fields[tempq.text] = forms.ChoiceField(label=tempq.text, choices=tempq.answers, required=True)