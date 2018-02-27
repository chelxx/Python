# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from .models import * #From Models import ALL
from time import gmtime, strftime
from datetime import datetime
import bcrypt
import re

# Create your views here.
def index(request):
    return render(request, 'class_app/index.html')

def register(request):
    print ('REGISTER VIEW')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.create(
            first = request.POST['first'],
            last = request.POST['last'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['user_id'] = user.id
        course = Course.objects.all()
        favorite = user.userfave.all()
        context = {
            'user' : user,
            'courses' : course,
            'favorite' : favorite
        }
    return render(request, 'class_app/success.html', context)

def login(request):
    print('LOGIN VIEW')
    errors = []
    try:
        u = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), (User.objects.filter(email=request.POST['email']))[0].password.encode()) == True:  
            print 'wizard'
            request.session['user_id'] = u.id 
            user = User.objects.get(id=u.id)
            return redirect('/success')
        else:
            errors.append('Invalid Password!')
    except:
        errors.append('Email does not exist!')
    print 'muggle'
    for error in errors:
        messages.error(request, error)
    return redirect('/')

def logout(request):
    print('LOGOUT VIEW')
    errors = []
    try:
        print ('TRY LOGOUT')
        del request.session['user_id']
        request.session.clear()
        errors.append('You have been logged out! Bye, dude!')
    except KeyError:
        print ('EXCEPT LOGOUT')
        pass    
    for error in errors:
        messages.error(request, error)
    return redirect('/')

def create(request):
    print('CREATE VIEW')
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/success')
    else:
        user = User.objects.get(id=request.session['user_id'])
        course = Course.objects.create(   
        description = request.POST['description'],
        course_name = request.POST['course_name'],
        creator = user
        )
        return redirect('/success')

def success(request):
    print('SUCCESS VIEW')
    today = datetime.now().date()
    user = User.objects.get(id=request.session['user_id'])
    course = Course.objects.all()
    favorite = user.userfave.all()
    context = {     
        'user' : user,
        'course' : course,
        'favorite' : favorite 
    }
    return render(request, 'class_app/success.html', context)

def edit(request, id):
    user = User.objects.get(id=request.session['user_id'])
    course = Course.objects.get(id=id) 
    context = {    
        'user' : user,
        'appoint' : appoint,
    }
    return render(request, 'class_app/edit.html', context)

def update(request, id):
    errors = Course.objects.course_validator(request.POST)
    if errors:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('/edit')
    else:
        course = Course.objects.get(id = id)
        course.description = request.POST['description']
        course.course_name = request.POST['course_name']
        course.save()
        return redirect('/success')

def delete(request, id):
    course = Course.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'course' : course,
    }
    return render(request, 'class_app/delete.html', context)

def favorite(request, id):
    course1 = Course.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    course1.favorites.add(user)
    course1.save()
    return redirect('/success')

def unfavorite(request, id):
    course1 = Course.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    course1.favorites.remove(user)
    course1.save()
    return redirect('/success')

def destroy(request, id):
    print('DESTROY VIEW')
    course = Course.objects.filter(id=id)
    course.delete()
    return redirect('/success')

