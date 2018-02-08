# MAKING DICTIONARIES

names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
        new_dict[list1[i]] = list2[i]
    print new_dict
        
make_dict(names, favorite_animal)

# Hacker Challenge

from random import choice

names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

def hacker(list1, list2):
    results = {x: choice(list2) for x in list1}
    print results

hacker(names, favorite_animal)

# END