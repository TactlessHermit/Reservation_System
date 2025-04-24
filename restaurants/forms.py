from django import forms
from .models import Restaurant

#Model Form
class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'
