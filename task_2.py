

class Car:
    def __init__(self):
        self.speed = 0
        self.wangle = 0
    def scanSpeed(self, speed,wangle):
        self.speed = speed
        self.wangle = wangle

    def printCar(self):

        return 'speed : {}\twangle {}\n'.format(self.speed, self.wangle)

    def acceleration(self, seconds):
        a = 0;
        while a < seconds:
            self.speed = self.speed + 10
            a = a + 1
            if (self.speed > 220):
                self.speed = 220
                print("The car accelerated,now car has she speed: ", self.speed)
                print("Car obtained the maximum speed")
                break

            else:
                print("The car accelerated,now car has she speed: ", self.speed)

    def deceleration(self, seconds):
        a = 0
        while a < seconds:
            self.speed = self.speed - 20
            a=a+1
            if (self.speed < 0):
                self.speed = 0
                print("The car stopped , now car has the speed :0")
                print("I did not have to climb mountains with such an old car")
                break
            else:
                print("The car decelerated,now car has she speed: ", self.speed)
    def left(self, degrees):
        a = 0;
        while a < degrees:
            self.wangle = self.wangle - 1
            a = a + 1
            if (self.wangle < -45):
                self.wangle = -45
                print("The car goes left with {} degrees ", self.wangle)
                print("Car obtained left extreme")
                break

            else:
                print("The car goes left with {} degrees ", self.wangle)
    def right(self, degrees):
        a = 0;
        while a < degrees:
            self.wangle = self.wangle + 1
            a = a + 1
            if (self.wangle > 45):
                self.wangle = 45
                print("The car goes right with {} degrees ", self.wangle)
                print("Car obtained right extreme")
                break

            else:
                print("The car goes right with {} degrees ", self.wangle)



car1=Car()
car1.scanSpeed(45,0)
print(car1.printCar())
while True:
    secret_word = input('enter a command: ')
    if secret_word[0] == "w":

        car1.acceleration(1)
        for s in secret_word.split():

            if s.isdigit():
                car1.acceleration(int(s)-1)
    if secret_word[0] == "s":
        car1.deceleration(1)
        for s in secret_word.split():

            if s.isdigit():
                car1.deceleration(int(s) - 1)
    if secret_word[0] == "a":
        car1.left(1)
        for s in secret_word.split():

            if s.isdigit():
                car1.left(int(s)-1)
    if secret_word[0] == "d":
        car1.right(1)
        for s in secret_word.split():

            if s.isdigit():
                car1.right(int(s)-1)
    if secret_word=="print":
        print(car1.printCar())
    if secret_word == "break":
        print("Game over")
        break
