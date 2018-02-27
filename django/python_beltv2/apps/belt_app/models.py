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
        if len(postData['first']) < 2: 
            errors.append('First name should be more than 2 characters.')
        if len(postData['last']) < 2:
            errors.append('Last name should be more than 2 characters.')

        # Name Character Validation
        if not postData['first'].isalpha():
            errors.append('First Name cannot contain numbers.')
        if not postData['last'].isalpha():
            errors.append('Last Name cannot contain numbers.')

        # Password Validation
        if len(postData['password']) < 8:
            errors.append('Password should be longer than 8 characters.')
        if postData['password'] != postData['confirm_password']:
            errors.append('Password do not match.')

        #Email Validation
        if len(self.filter(email = postData['email'])) > 1:
            errors.append('Email address is already in use.')
        return errors

class User(models.Model):
    first = models.CharField(max_length=255, default = 'blank')
    last = models.CharField(max_length=255, default = 'blank')
    email = models.CharField(max_length=255, default = 'blank')
    password = models.CharField(max_length=255, default = 'blank')
    birthday = models.DateField(auto_now=False, auto_now_add=False, default='blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

#MODELS FOR BELT EXAM HERE: