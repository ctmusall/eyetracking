from django import forms
from django.contrib.auth.models import User
from eyetracking.models import UserProfile, GatheredData

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )

class DataGather(forms.Form):
    location = forms.CharField(max_length = 50)
    speed = forms.CharField(max_length = 50)
    gaze = forms.CharField(max_length = 50)
    incident = forms.CharField(max_length = 50)
