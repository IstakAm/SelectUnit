# Generated by Django 4.1.1 on 2022-09-12 15:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0005_alter_course_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='exam',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 9, 12, 20, 12, 18, 203500)),
        ),
    ]
