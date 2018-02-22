# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error
# from datetime import datetime

from .models import User

# Create your VIEWS here.
#Views consist the bulk of your logic. I have basically none but I try.
#Use print statements ALL OVER your code to make sure things are working as they should.
def index(request):
    print ('GGGRRRR... THIS IS THE INDEX!!!!!!!')
    context = {
        'users': User.objects.all()
    } #Dictionary to hold a QUERY for use in the index.html page. We used User.objects.all() because we want to see ALL the data!
    return render(request, 'users_app/index.html', context) #Renders the template and CONTEXT is stated here because you want to pass that info onto the template

def new(request):
    print ('THIS IS THE FORM!!!!') #BLEH!
    return render(request, 'users_app/new.html') #Renders the template

def edit(request, id): #id is stated here because you want the id to be passed onto the URL
#FORM RENDERS BUT DOES NOT DO ANYTHING. EDIT AND UPDATE VIEWS NEEDS WORK!
    print ('THIS IS EDITING!!!!')
    user = User.objects.get(id=id) #QUERY to get specific id and attach it to a variable
    context = {
        'user': user
    } #Dictionary containing user information for use in this template/view
    return render(request, 'users_app/edit.html', context) 

def show(request, id): #id is stated here because you want the id to be passed onto the URL
    print ('THIS IS ME SHOWING YOU STUFF!!!!!')
    user = User.objects.get(id=id) #QUERY to get the id of the specific person to be displayed
    context = {
        'user': user
    } #Dictionary containing user information for use in this template/view
    return render(request, 'users_app/show.html', context) #Renders a template and CONTEXT is stated here because you want to pass that info onto the template

def create(request):
#USER IS CREATED BUT ERROR MESSAGES DO NOT APPEAR. FIX!
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print ('CREATE IF PATH')
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('/new') #If errors are prsent, stay in the new.html to flash the error messages
    else: #If there are NO errors, this code will execute and proceed to create a new user which will be added to the index.html
        print ('CREATE ELSE PATH')
        User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'],
        ) #QUERY that assigns variable names using the form inputs the user provided
        return redirect('/') #As soon the code is executes, a user is created, go back to index.html

def destroy(request, id): #The id is needed to attach to the URL to keep track of who's being deleted
    user = User.objects.get(id=id) #QUERY to get the specific id 
    user.delete() #User with the id is deleted
    return redirect('/') #Goes back to index.html once successful

def update(request):
#THIS DOES NOT WORK...
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print ('UPDATE IF PATH')
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('edit/'.format(id))
    else:
        print ('UPDATE ELSE PATH')
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        return redirect('/')