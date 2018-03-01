# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='blank', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='blank', max_length=50),
        ),
    ]