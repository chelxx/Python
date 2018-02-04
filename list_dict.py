# MAKING DICTIONARIES

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
        new_dict[list1[i]] = list2[i]
    print new_dict
        
make_dict(name, favorite_animal)

# END