# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from datetime import datetime
from .models import *
import bcrypt
import re

# Create your views here.
def index(request):
    print ('THERE ARE NO MISTAKES HERE, JUST HAPPY LITTLE ACCIDENTS. WOMP WOMP!') #I LIED THIS IS MISTAKE ISLAND :(
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
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
            birthday = request.POST['birthday'],
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
    appointment = Appointment.objects.all().order_by('appdate')
    context = {
        'user' : user,
        'appointment' : appointment,
    }
    return render(request, 'belt_app/success.html', context)

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

# EXAM :(
def add(request):
    errors = Appointment.objects.appointment_validator(request.POST)
    if errors:
        print ('IF - ADD')
        for error in errors:
            messages.error(request, error)
        return redirect('/success')
    else:
        print ('ELSE - ADD')
        appointment = Appointment.objects.create(
            appdate = request.POST['appdate'],
            apptime = request.POST['apptime'],
            apptask = request.POST['apptask']
        )
    return redirect('/success')

def edit(request, id):
    appointment = Appointment.objects.all()
    user = User.objects.get(id=request.session['user_id'])
    print ('EDIT FORM')
    context = {
        'user' : user,
        'appointment' : appointment
    }
    return render(request, 'belt_app/edit.html', context)

def update(request, id): #?????
    appointment_list = Appointment.objects.filter(id=id)
    if len(appointment_list) > 0:
        appointment = appointment_list[0]
        errors = Appointment.objects.validate(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
        else:
            appointment.apptask = request.POST['apptask']
            appointment.appdate = request.POST['appdate']
            appointment.apptime = request.POST['apptime']
            appointment.save()
            return redirect('/success')

def delete(request, id):
    appointment = Appointment.objects.filter(id=id)
    appointment.delete()
    return redirect('/success')