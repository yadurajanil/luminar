
from django import forms

from schoolapp.models import School


class Schoolform(forms.ModelForm):
    location_choices=[('ernamkulam','Ernamkulam'),('Calicut','Calicut'),('Thrissur','Thrissur')]
    location=forms.ChoiceField(choices=location_choices,widget=forms.Select,required=True)

    class Meta:
        model=School
        fields=['name','principal','location']
