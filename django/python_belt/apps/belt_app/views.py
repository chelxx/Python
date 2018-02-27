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
    if len(errors):
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
        request.session['user_id'] = user.id
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
    today = datetime.datetime.now().date()
    appointment = Appointment.objects.filter(creator=user).filter(appdate=today).order_by('appdate', 'apptime')
    appointment1 = Appointment.objects.filter(creator=user).exclude(appdate=today).order_by('appdate', 'apptime')
    context = {
        'user' : user,
        'appointment' : appointment,
        'appointment1' : appointment1,
    }
    print appointment
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

def add(request):
    errors = Appointment.objects.appointment_validator(request.POST)
    if errors:
        print ('IF - ADD')
        for error in errors:
            messages.error(request, error)
        return redirect('/success')
    else:
        print ('ELSE - ADD')
        user = User.objects.get(id=request.session['user_id'])
        appointment = Appointment.objects.create(
            appdate = request.POST['appdate'],
            apptime = request.POST['apptime'],
            apptask = request.POST['apptask'],
            creator = user,
        )
    return redirect('/success')

def edit(request, id):
    appointment = Appointment.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    # errors = Appointment.objects.appointment_validator(request.POST)
    # print ('EDIT FORM')
    # if errors:
    #     print ('IF - EDIT')
    #     for error in errors:
    #         messages.error(request, error)
    #     return redirect('/edit/{{ appointment.id }}')
    # else: 
    #     print ('ELSE - EDIT')
    #     context = {
    #         'user' : user,
    #         'appointment' : appointment,
    #     }
    #     return render(request, 'belt_app/edit.html', context)
    print ('ELSE - EDIT')
    context = {
        'user' : user,
        'appointment' : appointment,
    }
    return render(request, 'belt_app/edit.html', context)

def update(request, id):
    print('UPDATE VIEW')
    errors = Appointment.objects.appointment_validator(request.POST)
    if errors:
        print ('IF - UPDATE')
        for error in errors:
            messages.error(request, error)
        return redirect('/edit/{{ appointment.id }}')
    else:
        print ('ELSE - UPDATE')
        appointment = Appointment.objects.get(id=id)
        appointment.apptask = request.POST['apptask']
        appointment.appstat = request.POST['appstat']
        appointment.appdate = request.POST['appdate']
        appointment.apptime = request.POST['apptime']
        appointment.save()
        return redirect('/success')

def delete(request, id):
    appointment = Appointment.objects.filter(id=id)
    appointment.delete()
    return redirect('/success')