from django import forms

OPTIONS = (
    'Normal',
    'Morbidly Obese'
)

class DummyForm(forms.Form):
    example = forms.ChoiceField(choices=OPTIONS, required=True)
