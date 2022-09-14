import jdatetime
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, time
from django_jalali.db import models as jmodels


# Create your models here.



class Course(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)
    capacity = models.IntegerField(default=0)
    filled = models.IntegerField(default=0)
    units = models.IntegerField(default=0)
    master = models.CharField(max_length=256, blank=True, null=True)
    exam_date = jmodels.jDateField(default=jdatetime.datetime.now(), blank=False, null=False)
    exam_hour = models.TimeField(blank=False, null=True)
    place = models.CharField(max_length=128, blank=True, null=True)
    classTime = models.ManyToManyField('ClassTime', related_name='classtimes')
    coeducational = models.BooleanField(default=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)


    def __str__(self):
        return self.name


class ClassTime(models.Model):
    from_hour = models.TimeField(blank=False, null=True)
    to_hour = models.TimeField(blank=False, null=True)
    day = models.CharField(max_length=128, choices=(
        ('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'), ('5', 'Wednesday'), ('6', 'Thursday'),
        ('7', 'Friday')), blank=False, null=False)

    def __str__(self):
        if self.get_day_display()!='':
            return self.get_day_display()
        else:
            return self.day
