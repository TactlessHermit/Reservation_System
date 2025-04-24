from django import forms
from .models import Reservation
from restaurants.models import Restaurant


# Create your forms here.
class ReservationForm(forms.ModelForm):
    restaurant_name = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['restaurant_name'].choices = [(restaurant.id, restaurant.name)
                                                  for restaurant in Restaurant.objects.all()]

    class Meta:
        model = Reservation
        fields = ['date', 'time', 'restaurant_name']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }