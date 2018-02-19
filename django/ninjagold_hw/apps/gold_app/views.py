# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

# Create your views here.
def index(request):
    print ('INDEX')
    if 'gold_coins' not in request.session:
        request.session['gold_coins'] = 0
    if 'player_activities' not in request.session:
        request.session['player_activities'] = []
    return render(request, 'gold_app/index.html')
    
def process(request):
    # GAMBLING LOGIC HERE
    print ('I IS GAMBLING!')
    if request.POST['hideme'] == 'farm':
        gamble = random.randrange (10, 21)
        request.session['gold_coins'] += gamble
        update = "Earned " + str(gamble) + " gold coins from The Farm! (" + str(datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
        request.session['player_activities'].append(update)
        print ('I CLICKED ON FARM')
        print update
    if request.POST['hideme'] == 'cave':
        gamble = random.randrange (5, 11)
        request.session['gold_coins'] += gamble
        update = "Earned " + str(gamble) + " gold coins from The Farm! (" + str(datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
        request.session['player_activities'].append(update)
        print ('I CLICKED ON CAVE')
        print update
    if request.POST['hideme'] == 'house':
        gamble = random.randrange (2, 6)
        request.session['gold_coins'] += gamble
        update = "Earned " + str(gamble) + " gold coins from The Farm! (" + str(datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
        request.session['player_activities'].append(update)
        print ('I CLICKED ON HOUSE')
        print update
    if request.POST['hideme'] == 'casino':
        luck = random.randint(1,2)
        if luck == 1:
            gamble = random.randrange(0, 51)
            request.session['gold_coins'] += gamble
            update = "Entered The Casino and got " + str(gamble) + " gold coins! (" + str(datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
            request.session['player_activities'].append(update)
            print ('I WON')
            print update
        elif luck == 2:
            gamble = random.randrange(-50, 0)
            request.session['gold_coins'] += gamble
            update = "Entered The Casino and got " + str(gamble) + " gold coins! OUCH! *Gambling is no good! Escape while you can!*(" + str(datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
            request.session['player_activities'].append(update)
            print ('I LOST')
            print update
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')