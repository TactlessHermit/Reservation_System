import re

from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser
from django import forms

# Function to validate phone number input
def validate_phone_number(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Form for creating user accounts in webpages
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'First Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'Last Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'place_holder': 'Email',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'place_holder': 'Birthday',
        'type': 'date',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'place_holder': 'Password',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'place_holder': 'Re-enter Password',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={
        'place_holder': 'Phone Number',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_phone_number])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1',
                  'password2', 'birthday', 'phone_no']
