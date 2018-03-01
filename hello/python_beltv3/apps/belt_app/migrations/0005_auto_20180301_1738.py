# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0004_auto_20180301_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertrips', to='belt_app.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='favorites',
            field=models.ManyToManyField(related_name='userfaves', to='belt_app.User'),
        ),
    ]
