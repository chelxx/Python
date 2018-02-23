# -*- coding: utf-8 -*-


# Create your models here.
from __future__ import unicode_literals

from django.db import models



# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        # Courses name
        if len(postData['course_name']) > 5: 
            errors.append("Course name needs to be longer than five characters")
   
        # description 
        if len(postData['description']) < 15:
            errors.append("Description needs to be longer than 15 characters")
       
            print 'wizard'



class Course(models.Model):
    course_name = models.CharField(max_length=255, default = 'blank')
    description = models.CharField(max_length=255, default = 'blank')
    created_at = models.DateTimeField(auto_now_add = True)


    objects = CourseManager()