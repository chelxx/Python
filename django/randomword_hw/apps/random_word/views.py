# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=32, allowed_chars='CATS')


# Create your views here.
def index(request):
    print ('INDEX')
    return render(request, 'random_word/index.html')

def generate(request):
    print ('GENERATE')
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    unique_id = get_random_string(length=32, allowed_chars='ILOVECATS')
    words = {
        'random_word': unique_id
    }
    return render(request, 'random_word/index.html', words)

def reset(request):
    print ('RESET')
    # RESET COUNTER HERE
    request.session.clear()
    return redirect('/')