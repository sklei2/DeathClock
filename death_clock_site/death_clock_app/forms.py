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

class LoginForm(forms.Form):
	username = forms.CharField(required=True, label='Username')
	password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)


class UserSignupForm(forms.Form):
	username = forms.CharField(required=True,
							   label='Username')
	pwd = forms.CharField(required=True,
						  widget=forms.PasswordInput(),
						  label='Password')

	pwd_check = forms.CharField(required=True,
								widget=forms.PasswordInput(),
								label='Confirm Password')

	def __init__(self, *args, **kwargs):
		super(UserSignupForm, self).__init__(*args, **kwargs)

	def clean(self):
		try:
			errors = []
			if self.cleaned_data['pwd'] != self.cleaned_data['pwd_check']:
				errors.append("Passwords do not match")
			if any(errors):
				raise forms.ValidationError(errors)
		except KeyError:
			pass
		return self.cleaned_data
