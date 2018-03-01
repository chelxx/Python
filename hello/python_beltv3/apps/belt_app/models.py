# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        # Name Length Validation
        if len(postData['name']) < 3: 
            errors.append('Name should be more than 3 characters.')
        if len(postData['username']) < 3:
            errors.append('Username should be more than 3 characters.')

        # Name Character Validation
        # if not postData['name'].isalpha():
        #     errors.append('Name cannot contain numbers.')

        # Password Validation
        if len(postData['password']) < 8:
            errors.append('Password should be longer than 8 characters.')
        if postData['password'] != postData['confirm_password']:
            errors.append('Password do not match.')

        #Email Validation
        if len(self.filter(username = postData['username'])):
            errors.append('Username is already in use.')
        return errors

class User(models.Model):
    name = models.CharField(max_length=50, default = 'blank')
    username = models.CharField(max_length=50, default = 'blank')
    password = models.CharField(max_length=255, default = 'blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

#BELT EXAM MODELS HERE:

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = []
        curr_date = unicode(datetime.datetime.now())
        if len(postData['destination']) < 3: 
            errors.append('Destination should be more than 3 characters.')
        if len(postData['description']) < 3:
            errors.append('Description should be more than 3 characters.')
        if len(postData['trip_start']) == 0 or len(postData['trip_end']) == 0:
            errors.append('Dates cannot be blank!')
        if curr_date > postData['trip_start']:
            errors.append('Time travel is illegal, son!')
        # if postData['trip_end'] > postData['trip_start']:
        #     errors.append('Time travel is illegal, son! *')
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    trip_start = models.DateField(auto_now=False, auto_now_add=False)
    trip_end = models.DateField(auto_now=False, auto_now_add=False)
    creator = models.ForeignKey(User, related_name="usertrips")
    favorites = models.ManyToManyField(User, related_name="userfaves") #Many to Many Relationship

    objects = TripManager()
