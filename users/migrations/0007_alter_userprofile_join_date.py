# Generated by Django 4.1.1 on 2022-09-12 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 22, 40, 20, 426816)),
        ),
    ]