# Car Assignment

class Car(object):
    def __init__(self, name, price, fuel, speed, mileage):
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def information(self):
        print ("Brand: {}").format(self.name)
        print ("Price: {}").format(self.price)
        print ("Speed: {}").format(self.speed)
        print ("Fuel: {}").format(self.fuel)
        print ("Mileage: {}").format(self.mileage)
        if self.price < 10000:
            print ("Tax: 12%")
        if self.price > 10000:
            print ("Tax: 15%")
        

def display_all():
    honda = Car("Honda", 2000, "Full", "10mph", "15mpg")
    hyundai = Car("Hyundai", 4000, "Empty", "20mph", "25mpg")
    nissan = Car("Nissan", 600, "Full", "30mph", "35mpg")
    toyota = Car("Toyota", 800, "Empty", "40mph", "45mpg")
    benz = Car("Mercedez Benz", 10000, "Full", "50mph", "55mpg")
    lambo = Car("Lamborghini", 12000, "Empty", "60mph", "65mpg")

    honda.information()
    hyundai.information()
    nissan.information()
    toyota.information()
    benz.information()
    lambo.information()

display_all()

# END