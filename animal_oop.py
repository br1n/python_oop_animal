class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "{} health: {}".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Dog", 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("Dragon", 170)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "This is a Dragon"
        return self

rat = Animal("Rat", 50)
print "*" * 50
rat.display_health()
# print rat.pet() #does not work - no attribute "pet"
# print rat.fly() #does not work - no attribute "fly"

print "*" * 50
print Dog().walk().walk().walk().run().run().pet().display_health()
#print Dog().fly() #does not work - no attribute "fly"
print "*" * 50
Dog().pet().display_health()

print "*" * 50
print Dragon().fly().display_health()
#print Dragon().pet().display_health() #does not work - no attribute "fly"




    


