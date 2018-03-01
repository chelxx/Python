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
            date_hired = request.POST['date_hired'], 
        ) 
        request.session['user_id'] = user.id
        item = Item.objects.all()
        context = {
            'user' : user,
            'item' : item,
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

def success(request): #NOTES: I still need to figure out how to display the names instead of the ID
    print('SUCCESS VIEW')
    user = User.objects.get(id=request.session['user_id'])
    item = Item.objects.all().order_by('created_at')
    wish = user.wishlist.all().order_by('created_at')
    context = {
        'user' : user,
        'item' : item,
        'wish' : wish,
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

#VIEWS FOR BELT EXAM HERE
def add_item(request):
    print('ADD ITEM FORM')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : user,
    }
    return render(request, 'belt_app/add.html', context)

def create_item(request):
    print('CREATE ITEM VIEW')
    errors = Item.objects.item_validation(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/success')
    else:
        user = User.objects.get(id=request.session['user_id'])
        print('ACTUALLY CREATING')
        item = Item.objects.create(
            item_name = request.POST['item_name'],
            creator = user
        ) 
        return redirect('/success')

def show_item(request, id):
    print('SHOW ITEM VIEW')
    user = User.objects.get(id=request.session['user_id'])
    item = Item.objects.get(id=id)
    context = {
        'user' : user,
        'item' : item,
    }
    return render(request, 'belt_app/show.html', context)

def add_wish(request, id):
    wish_item = Item.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    wish_item.wishlist.add(user)
    wish_item.save()
    return redirect('/success')

def remove_wish(request, id):
    wish_item = Item.objects.filter(id=id)[0]
    user = User.objects.get(id=request.session['user_id'])
    wish_item.wishlist.remove(user)
    wish_item.save()
    return redirect('/success')

def delete(request, id):
    print('DELETE VIEW')
    item = Item.objects.filter(id=id)
    item.delete()
    return redirect('/success')