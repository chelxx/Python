# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from .models import *
import bcrypt
import re
# NAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]

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
    try:
        print ('TRY ME BITCH')
        user = User.objects.filter(email = request.POST['email'])
    except:
        print ('EXCEPT')
        messages.add_message(request, messages.INFO, 'The email address or password are incorrect')
        return redirect
    if bcrpyt.checkpw(request.POST['password'].encode(), user.password.encode()) == True: # Changes - true statement
        print ('GOT INTO BCRYPT')
        request.session['logged_in'] = user.email
        request.session['first'] = user.first 
        
        return redirect(request, 'login_app/success.html', context)


def success(request):
    print('SUCCESS VIEW')
    return render(request, 'login_app/success.html')

def logout(request):
    print('LOGOUT VIEW')
    request.session.delete() #CHANGED from delete.session()
    return redirect('/')
