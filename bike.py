# Bike Assignment

class Bike(object):
    def __init__(self, name, price, speed, miles):
        self.name = name
        self.price = price
        self.speed = speed
        self.miles = miles

    def brand(self):
        print("The bike's brand is {}.".format(self.name))

    def cost(self):
        print("The bike costs ${}".format(self.price))

    def ride(self):
        print("Adding... From {} mph, now it's {} mph! So fast!".format(self.speed, (self.speed + 10)))
    
    def reverse(self):
        print("Reducing... From {} miles, the current total is {} miles!".format(self.miles, (self.miles - 5)))

def displayinfo():
    schwinn = Bike("Schwinn", 100, 25, 100)

    schwinn.brand()
    schwinn.cost()
    schwinn.ride()
    schwinn.reverse()

displayinfo()

# END