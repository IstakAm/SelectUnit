# Generated by Django 4.1.1 on 2022-09-12 12:37

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_alter_course_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='exam',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 9, 12, 17, 7, 52, 557699)),
        ),
    ]
