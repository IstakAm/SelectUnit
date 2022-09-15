from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.forms import DateInput

from .models import Course, ClassTime
from users.models import CourseStack
from tempus_dominus.widgets import DateTimePicker


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['user', 'classTime']
        widgets = {
            'exam': DateTimePickerInput()
        }


class ClassTimeForm(forms.ModelForm):
    class Meta:
        model = ClassTime
        fields = '__all__'

