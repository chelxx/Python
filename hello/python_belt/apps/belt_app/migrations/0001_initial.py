# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appdate', models.DateField()),
                ('apptime', models.TimeField()),
                ('apptask', models.CharField(default='blank', max_length=255)),
                ('appstat', models.CharField(default='Pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(default='blank', max_length=255)),
                ('last', models.CharField(default='blank', max_length=255)),
                ('email', models.CharField(default='blank', max_length=255)),
                ('password', models.CharField(default='blank', max_length=255)),
                ('birthday', models.DateField(default='blank')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userappts', to='belt_app.User'),
        ),
    ]
