# Animal Assignment

class Animal(object): #parent
    def __init__ (self, name, health):
        self.name = name
        self.health = health
        
    def walk(self): #method
        self.health -= 1
        print ("After walkies, {}'s health is now {}.").format(self.name, self.health)
        return self

    def run(self): #method
        self.health -= 5
        print ("After zoomies, {}'s health is now {}.").format(self.name, self.health)
        return self

    def displayHealth(self):
        if isinstance (self, Dragon):
            print ("I'm a dragon!")
        else:
            print self.name, self.health 
        return self

class Doggy(Animal):
    def __init__ (self, name, health = 150):
        Animal.__init__ (self, name, health)

    def pet(self):
        self.health += 5
        print ("After petting, {}'s health is now {}.").format(self.name, self.health)
        return self

class Dragon(Animal):
    def __init__ (self, name, health = 170, ):
        Animal.__init__ (self, name, health)

    def fly(self):
        self.health -= 10
        print ("After flying, {}'s health is now {}.").format(self.name, self.health)
        return self

def main():

    dog = Doggy("Doug").walk().walk().walk().run().run().pet().displayHealth()
    dragon = Dragon("Falcor").fly().fly().fly().displayHealth()

main()
# WIP