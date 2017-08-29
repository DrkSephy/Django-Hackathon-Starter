from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from models import UserProfile
from models import PhotoRequest

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True)

class PhotoRequestForm(forms.ModelForm):
    class Meta:
        model = PhotoRequest
        fields = ['first_name', 'last_name', 'department', 'event', 'description', 'start_date_time', 'end_date_time']