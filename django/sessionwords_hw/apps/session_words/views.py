# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):
    # response = 'SUP'
    # return HttpResponse(response)
    if 'new_words' not in request.session:
        request.session['new_words'] = []
    print ('INDEX')
    return render(request, 'session_words/index.html')

def process(request):
    update = request.POST['given_word']
    request.session['new_words'].append(update)
    print update
    print request.session['new_words']
    return redirect('/')

def reset(request):
    request.session.clear()
    print ('SESSION CLEARED?')
    return redirect('/')