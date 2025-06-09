from django.contrib.auth.forms import UserCreationForm

from multiapp.models import CustomUser
from django import forms

class Customusercreationform(UserCreationForm):
    gender_choices=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect,required=True)
    role_choices=[('student','student'),('teacher','teacher')]
    role=forms.ChoiceField(choices=role_choices,widget=forms.Select,required=True)

    class Meta:
        model=CustomUser
        # fields=['username','password','password1','phone','gender','first_name','last_name','role']
        fields=UserCreationForm.Meta.fields+('phone','gender','email','first_name','last_name','role')