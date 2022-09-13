# Generated by Django 4.1.1 on 2022-09-12 12:36

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('day', models.CharField(choices=[('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'), ('5', 'Wednesday'), ('6', 'Thursday'), ('7', 'Friday')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(default=0)),
                ('filled', models.IntegerField(default=0)),
                ('units', models.IntegerField(default=0)),
                ('master', models.CharField(blank=True, max_length=256, null=True)),
                ('exam', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 9, 12, 17, 6, 26, 301152))),
                ('place', models.CharField(blank=True, max_length=128, null=True)),
                ('coeducational', models.BooleanField(default=True)),
                ('classTime', models.ManyToManyField(to='units.classtime')),
            ],
        ),
    ]
