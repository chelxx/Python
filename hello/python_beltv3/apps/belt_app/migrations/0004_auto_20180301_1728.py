# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='trips_dude',
        ),
        migrations.AddField(
            model_name='trip',
            name='favorites',
            field=models.ManyToManyField(related_name='userfave', to='belt_app.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_start',
            field=models.DateField(),
        ),
    ]
