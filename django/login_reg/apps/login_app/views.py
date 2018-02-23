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
    return render(request, 'login_app/index.html')

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
        context = {
            'user' : user
        }
    return render(request, 'login_app/success.html', context)

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
    

def success(request):
    print('SUCCESS VIEW')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }
    return render(request, 'login_app/success.html', context)

def logout(request):
    print('YOU IS LOGGED OUT BITCH')
    try:
        print ('TRY LOGOUT')
        del request.session['user_id']
    except KeyError:
        print ('EXCEPT LOGOUT')
        pass
    return redirect('/')