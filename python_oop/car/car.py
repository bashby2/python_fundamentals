class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 15000:
            self.tax = 0.15
        else:
            self.tax = 0.12


    def displayall(self):
        print 'Price:$' + str(self.price)
        print 'Speed:' + str(self.speed) + 'mph'
        print 'Fuel:' + str(self.fuel)
        print 'Mileage:' + str(self.mileage) + 'mpg'
        print 'Tax:' +str(self.tax)

#Creating instances
car1 = Car(200000, 2, 'way too full', 8)
car1.displayall()

car2 = Car(22, 200, 'totally empty', 0)
car2.displayall()

car3 = Car(2000, 55, 'no idea', 25)
car3.displayall()

car4 = Car(1900, 47, 'full!', 14)
car4.displayall()

car5 = Car(526, 20, 'full', 55)
car5.displayall()

racecar = Car(99999999.01, 'way fast', 'runs on H2', 100000)
racecar.displayall()
