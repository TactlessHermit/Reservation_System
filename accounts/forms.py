import re
import phonenumbers

from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from phonenumbers import NumberParseException

from .models import CustomUser
from django import forms


# Function to validate phone number input
def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value)
    except NumberParseException:
        raise ValidationError("ERROR:: Invalid phone number. Phone number MUST be valid AND contain the CORRECT country/region code.")

    if not phonenumbers.is_valid_number(parsed_number):
        raise ValidationError("ERROR:: Invalid phone number. Phone number MUST be valid AND contain the CORRECT country/region code.")

# Function to validate name inputs
def validate_names(value):
    if re.search(r'\d', value):
        raise ValidationError("ERROR:: Names can't contain numbers.")

# Form for creating user accounts
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'First Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_names])
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'Last Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_names])
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
    phone_no = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
        'place_holder': 'Phone Number',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_phone_number])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1',
                  'password2', 'birthday', 'phone_no', 'photo']


# Form for updating user accounts
class CustomUserChangeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'First Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_names])
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'Last Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }), validators=[validate_names])
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'place_holder': 'Birthday',
        'type': 'date',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    phone_no = forms.CharField(max_length=15,
                               widget=forms.TextInput(attrs={
                                   'place_holder': 'Phone Number',
                                   'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
                               }), validators=[validate_phone_number])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birthday', 'phone_no', 'photo']