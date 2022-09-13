import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from units.models import Course


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=128, primary_key=False, blank=True, null=True)
    join_date = models.DateTimeField(default=datetime.datetime.now(), blank=False, null=False)


class CoursePlace(models.Model):
    row = models.IntegerField(default=0, blank=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)


class CourseStack(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField(CoursePlace, null=True)


class UnitsTable(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
    courses = models.ManyToManyField(CoursePlace, null=True)
