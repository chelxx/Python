# Bike Assignment

class Bike(object):
    def __init__(self, name, price, speed, miles):
        self.name = name
        self.price = price
        self.speed = speed
        self.miles = miles

    def brand(self):
        print("The bike's name is {}.".format(self.name))

    def cost(self):
        print("The bike costs ${}.".format(self.price))

    def ride(self):
        print("Riding...").format(self.miles)
    
    def reverse(self):
        print("Reversing...").format(self.miles)

def displayinfo():
    bike1 = Bike("Shirley", 100, 25, 50)
    bike2 = Bike("Ron", 150, 20, 60)

    bike1.brand()
    bike1.cost()
    bike1.ride()
    bike1.reverse()

displayinfo()

# END