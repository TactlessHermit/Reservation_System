from django import forms
from .models import Restaurant, Tag

#Model Form
class RestaurantForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(choices=[],
                                     widget=forms.CheckboxSelectMultiple
                                     )

    # GET ALL TAGS FROM TABLE
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(tag.id, tag.name)
                                                  for tag in Tag.objects.all()]

    class Meta:
        model = Restaurant
        fields = '__all__'
