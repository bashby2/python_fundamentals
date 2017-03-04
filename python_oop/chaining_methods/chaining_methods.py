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
        return self

    def ride(self):
        self.miles += 10
        print 'Ridin'
        return self

    def reverse(self):
        print 'Reversing. How does a bike reverse?'
        if self.miles > 5:
            self.miles -= 5
        return self

bike1 = Bike(2, 95)
bike2 = Bike(22, 5)
bike3 = Bike(222, 16)

bike1.ride().ride().ride().reverse().displayInfo()
