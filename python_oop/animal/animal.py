class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print 'Animal Name: ' + self.name
        print 'Animal Health: ' + str(self.health)


animal = Animal('animal')

animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        self.health = 150
        self.name = name

    def pet(self):
        self.health += 5
        return self

champ = Dog('champ')
champ.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        self.health = 170
        self.name = name

    def fly(self):
        self.health -= 10
        print 'This is a dragon!'
        return self

zippy = Dragon('Zippy')
zippy.walk().walk().walk().run().run().fly().fly().displayHealth()
# animal.fly().pet().displayHealth()
