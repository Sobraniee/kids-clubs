from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2')