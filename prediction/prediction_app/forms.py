from django import forms

CHOICES = (('1', 'Yes',), ('0', 'No',))


class FormName(forms.Form):
    house = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    age = forms.IntegerField()
    money = forms.IntegerField()
