# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

# Create your models here.
#OMG This is so hard to understand but here we go...
class UserManager(models.Manager):
#I DO NOT THINK THIS WORKS...
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First Name must be more than 1 characters!"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last Name must be more than 1 characters!"
        if 'email' in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "Invalid Email address!"
        return errors

class User(models.Model): #This is our TABLE! Assigning column names and their type
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()