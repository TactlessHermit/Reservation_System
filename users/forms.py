from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=1000)
    last_name = forms.CharField(max_length=1000)
    birthday = forms.DateField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'birthday']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
