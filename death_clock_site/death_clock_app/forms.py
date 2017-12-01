from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime


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

    SEX_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female')
    }

    # Username
    username = forms.CharField(required=True,
                               label='Username')
    # Password
    pwd = forms.CharField(required=True,
                          widget=forms.PasswordInput(),
                          label='Password')
    pwd_check = forms.CharField(required=True,
                                widget=forms.PasswordInput(),
                                label='Confirm Password')
    # Profile Information
    sex = forms.ChoiceField(SEX_CHOICES,
                            required=True,
                            label='Biological Sex')
    todays_date = datetime.date.today().year
    years_before = 100
    dob = forms.DateField(widget=SelectDateWidget(years=range(todays_date - years_before, todays_date)),
                          required=True,
                          label='Date Of Birth')

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

    def register(self):
        # generate the user as we normally would
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            password=self.cleaned_data['pwd'])

        new_user.save()

        # create the profile with our data
        sex = self.cleaned_data['sex']
        dob = self.cleaned_data['dob']
        new_user.profile.sex = sex
        new_user.profile.dob = dob
        new_user.profile.save()

        return new_user
