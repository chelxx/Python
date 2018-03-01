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
    print ('THERE ARE NO MISTAKES HERE, JUST HAPPY LITTLE ACCIDENTS. WOMP WOMP!')
    return render(request, 'belt_app/index.html')

def register(request): #YOU MIGHT WANT TO ADD SHIT HERE
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
            name = request.POST['name'],
            username = request.POST['username'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
        ) 
        request.session['user_id'] = user.id
        all_trips = Trip.objects.all()
        context = {
            'user' : user,
            'all_trips' : all_trips,
        }
    return render(request, 'belt_app/success.html', context)

def login(request):
    print('LOGIN VIEW')
    errors = []
    try:
        print ('TRY - LOGIN')
        u = User.objects.get(username=request.POST['username'])
        if bcrypt.checkpw(request.POST['password'].encode(), (User.objects.filter(username=request.POST['username']))[0].password.encode()) == True:  
            request.session['user_id'] = u.id 
            user = User.objects.get(id=u.id)
            return redirect('/success')
        else:
            errors.append('Invalid Password!')
    except:
        print ('EXCEPT - LOGIN')
        errors.append('Username does not exist!')
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

#BELT EXAM VIEWS HERE:

def success(request):
    print('SUCCESS VIEW')
    user = User.objects.get(id=request.session['user_id'])
    my_trip = user.userfaves.all().order_by('creator_id')
    all_trips = Trip.objects.all().order_by('creator_id')
    context = {
        'user' : user,
        'my_trip' : my_trip,
        'all_trips' : all_trips,
    }
    return render(request, 'belt_app/success.html', context)

def add_form(request):
    print('ADD TRIP FORM')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'belt_app/add_trip.html', context)

def add_trip(request):
    print('ADD TRIP VIEW')
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/add_form')
    else:
        user = User.objects.get(id=request.session['user_id'])
        print('ACTUALLY CREATING')
        item = Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            trip_start = request.POST['trip_start'],
            trip_end = request.POST['trip_end'],
            creator = user,
        ) 
        return redirect('/success')

def show_trip(request, id):
    print('SHOW TRIP VIEW')
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    context = {
        'user' : user,
        'trip' : trip,
    }
    return render(request, 'belt_app/show_trip.html', context)

def my_trip(request, id):
    print('ADDING A TRIP TO MY TRIPS')
    my_trip = Trip.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    my_trip.favorites.add(user)
    my_trip.save()
    return redirect('/success')

def remove_my_trip(request, id):
    print('REMOVING A TRIP FROM MY TRIPS')
    my_trip = Trip.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    my_trip.favorites.remove(user)
    my_trip.save()
    return redirect('/success')

def delete(request, id):
    print('DELETE VIEW')
    my_trip = Trip.objects.filter(id=id)
    my_trip.delete()
    return redirect('/success')