from django import forms
from django.contrib.auth.models import User
from eyetracking.models import GatheredData

class UserForm(forms.ModelForm):

    first_name = forms.CharField(label = 'First Name')
    last_name = forms.CharField(label = 'Last Name')
    email = forms.CharField(label = 'Email')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class DataGather(forms.Form):
    location = forms.CharField(max_length = 50)
    speed = forms.IntegerField()
    gaze = forms.CharField(max_length = 50)
    incident = forms.CharField(max_length = 50)
