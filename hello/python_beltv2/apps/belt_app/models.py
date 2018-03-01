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
            errors.append('First name should be more than 3 characters.')
        if len(postData['username']) < 3:
            errors.append('Last name should be more than 3 characters.')

        # Name Character Validation
        if not postData['name'].isalpha():
            errors.append('First Name cannot contain numbers.')

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
    # email = models.CharField(max_length=255, default = 'blank')
    password = models.CharField(max_length=255, default = 'blank')
    date_hired = models.DateField(auto_now=False, auto_now_add=False, default='blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

#MODELS FOR BELT EXAM HERE:
class ItemManager(models.Manager):
    def item_validation(self, postData):
        errors = []
        # Item Validation
        if len(postData['item_name']) < 3: 
            errors.append('Item name should be more than 3 characters.')
        return errors

class Item(models.Model):
    item_name = models.CharField(max_length=50, default = 'blank')
    creator = models.ForeignKey(User, related_name='item_users')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    wishlist = models.ManyToManyField(User, related_name ="wishlist")

    objects = ItemManager()