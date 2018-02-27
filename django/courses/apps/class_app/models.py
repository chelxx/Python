# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData): #Does all the validations for the Login/Registration
        errors = []
        # First Name Validations - it cannot be less than 2 character or contain numbers
        if len(postData['first']) < 2:
            errors.append("First name should be more than 2 characters.")
        if not postData['first'].isalpha():
            errors.append("First Name cannot contain numbers.")

        # Last Name Validations - it cannot be less than 2 character or contain numbers
        if len(postData['last']) < 2: 
            errors.append("Last name should be more than 2 characters.")
        if not postData['last'].isalpha():
            errors.append("Last Name cannot contain numbers.")

        # Password Validation - it cannot be less than 8 characters and it must match!
        if len(postData['password']) < 8:
            errors.append("Password should be longer than 8 characters.")
        if postData['password'] != postData['confirm_password']:
            errors.append("Password do not match.")

        #Email Validation - LOGIN! This will search for an existing email in the database
        if len(postData['email']) < 0:
            errors.append("Email must be filled out.")
        if len(self.filter(email = postData['email'])) > 1:
            errors.append('Email address is already in use.')
        return errors

class User(models.Model): #User table
    first = models.CharField(max_length=255, default = 'blank')
    last = models.CharField(max_length=255, default = 'blank')
    email = models.CharField(max_length=255, default = 'blank')
    password = models.CharField(max_length=255, default = 'blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class CourseManager(models.Manager): 
    def course_validator(self, postData): #Does all the validations for the Course
        errors = []
        #Description Validation - 
        if len(postData['description']) < 15:
            errors.append("Description must be more than 15 characters.")

        #Course Name Validation
        if len(postData['course_name']) < 5:
            errors.append("Course name must be more than 5 characters.")
        return errors

class Course(models.Model): #Course Table
    description = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name ="userappts")
    favorites = models.ManyToManyField(User, related_name ="userfave") #Many to Many Relationship

    objects = CourseManager()