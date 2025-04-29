from django import forms
from .models import Restaurant, Tag

#Model Form
class RestaurantForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'Name',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'place_holder': 'Location',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    tags = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple(attrs={
        'place_holder': 'Select Tags',
        'class': 'mt-2 bg-transparent w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))

    # GET ALL TAGS FROM TABLE
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(tag.id, tag.name)
                                                  for tag in Tag.objects.all()]

    class Meta:
        model = Restaurant
        fields = '__all__'
