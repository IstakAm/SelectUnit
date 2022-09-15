from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from units.models import *
from users.models import CourseStack


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CourseStackForm(forms.ModelForm):
    class Meta:
        model = CourseStack
        fields = ['name']

    courses = forms.CheckboxSelectMultiple()
