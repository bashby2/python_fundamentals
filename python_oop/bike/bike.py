class Bike(object):
    def __init__(self, price, speed):
        print 'My Bike!'
        self.brand = "Giant"
        self.color = "gold"
        self.age = 2
        self.speed = speed
        self.price = price
        self.fun_level = "Max"
        self.miles = 0

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Speed is:' + str(self.speed)
        print 'Total miles riden:' + str(self.miles)

    def ride(self):
        self.miles += 10
        print 'Ridin'

    def reverse(self):
        print 'Reversing. How does a bike reverse?'
        self.miles -= 5

bike1 = Bike(200, 25)
bike2 = Bike(150, 15)
bike3 = Bike(300, 30)
