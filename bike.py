# Bike Assignment

class Bike(object):
    def __init__(self, name, speed, miles):
        self.name = name
        self.speed = speed
        self.miles = miles
    
    def information(self):
        print (self.name, self.speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        if self.miles <= 0:
            self.miles = 0
        print(("Riding..."), self.miles)
        return self
    
    def reverse(self):
        self.miles -= 5
        if self.miles <= 0:
            self.miles = 0
        print(("Reversing..."), self.miles)
        return self

def displayinfo():
    bike1 = Bike("Harry", 25, 50).information().ride().ride().ride().reverse()
    bike2 = Bike("Ron", 20, 60).information().ride().ride().reverse().reverse()
    bike3 = Bike("Hermione", 30, 70).information().reverse().reverse().reverse()

displayinfo()

# END