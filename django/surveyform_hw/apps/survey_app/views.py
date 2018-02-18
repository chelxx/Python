# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    print 'Hello'
    return render(request, 'survey_app/index.html')

def process(request):
    print ('PROCESS')
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    context = {
        'name' : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['language'],
        'comments' : request.POST['comments'],
    }
    return render(request, 'survey_app/result.html', context)

def back(request):
    print ('RESULT')
    return redirect('/')
