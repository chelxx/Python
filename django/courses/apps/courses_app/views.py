
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from .models import *



# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses
    }


    
    print(context)
    return render(request, 'courses_app/index.html', context)


def create(request):
#USER IS CREATED BUT ERROR MESSAGES DO NOT APPEAR. FIX!
    errors = Course.objects.basic_validator(request.POST)
    if (errors):
        print ('CREATE IF PATH')
        for error in errors.iteritems():
            messages.error(request, error)
        
        return redirect('courses/')
    else:
        print ('CREATE ELSE PATH')
        Course.objects.create(
            course_name=request.POST['course_name'], 
            description=request.POST['description'], 
            # email=request.POST['email'],
        )
       
        return redirect('courses/')



def destroy(request, id):
    print "delete is working"
    course = Course.objects.get(id=id)
    course.delete()
    return render(request, 'courses_app/delete.html')

