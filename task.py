class Car:
    def scanSpeed(self,speed):
        self.speed=speed
    def printSpeed(self):
        print(" speed : %s" %self.speed)
    def acceleration(self,seconds):
        a=0;
        while a<seconds:
            self.speed=self.speed+10
            a=a+1
            if(self.speed>220):
                self.speed=220
                print("The car accelerated,now car has she speed: ",self.speed)
                print("Car obtained the maximum speed")
                break
            else:
                print("The car accelerated,now car has she speed: ",self.speed)
    def mountain_inclination(self,seconds):
        print("WOW! I see the mountains on the horizon")
        a=0
        while a<seconds:
            if self.speed>0:
                self.speed=self.speed-20
                print("Attention, the speed of the car decreases,now car has she speed: ",self.speed)
            else:
                self.speed=0
                print("The car stopped , now car has the speed :0")
                print("I did not have to climb mountains with such an old car")
                break




car1=Car()
car1.scanSpeed(45)
car1.printSpeed()
car1.acceleration(3)
car1.printSpeed()
car1.acceleration(40)
car1.mountain_inclination(10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   1,1        
