# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from .models import *
import bcrypt
import re

# Create your views here.
def index(request):
    print ('THERE ARE NO MISTAKES HERE, JUST HAPPY LITTLE ACCIDENTS. WOMP WOMP!') #SEND HALP
    return render(request, 'belt_app/index.html')

def register(request):
    print ('REGISTER VIEW')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        print ('IF - REGISTER')
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        print ('ELSE - REGISTER')
        user = User.objects.create(
            first = request.POST['first'],
            last = request.POST['last'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        ) 
        context = {
            'user' : user
        }
    return render(request, 'belt_app/success.html', context)

def login(request):
    print('LOGIN VIEW')
    errors = []
    try:
        print ('TRY - LOGIN')
        u = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), (User.objects.filter(email=request.POST['email']))[0].password.encode()) == True:  
            request.session['user_id'] = u.id 
            user = User.objects.get(id=u.id)
            return redirect('/success')
        else:
            errors.append('Invalid Password!')
    except:
        print ('EXCEPT - LOGIN')
        errors.append('Email does not exist!')
    for error in errors:
        messages.error(request, error)
    return redirect('/')
    

def success(request):
    print('SUCCESS VIEW')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }
    return render(request, 'belt_app/success.html', context)

def logout(request):
    print('LOGOUT VIEW')
    errors = []
    print ('TRY - LOGOUT')
    del request.session['user_id']
    errors.append('You have been logged out! Bye, dude~')
    for error in errors:
        messages.error(request, error)
    return redirect('/')