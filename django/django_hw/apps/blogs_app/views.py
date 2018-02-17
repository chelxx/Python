# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Placeholder to later display the list of blogs."
    # print "HELLO"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a NEW blog."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder to DISPLAY blog number: "
    return HttpResponse(response + number)

def edit(request, number):
    response = "Placeholder to EDIT blog number: "
    return HttpResponse(response + number)

def destroy(request, number):
    return redirect('/')