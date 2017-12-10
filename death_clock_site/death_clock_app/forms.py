from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
import datetime
from .PopulateSurveyTables import populateSurveyTables
from .models import *


# Question form
class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        #if no questions, then populate survey tables in db
        if len(Question.objects.all()) == 0:
            populateSurveyTables()

        for q in Question.objects.all():
            self.fields[q.question] = forms.BooleanField(label=q.question,required=False)


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True,
                               label='Password')

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
    sex = forms.ChoiceField(choices=SEX_CHOICES,
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
