import random

class vehicle:
    def __init__(self):
        self.speed=0
    
    def accelerate(self):
        self.speed+=1

    def decelerate(self):
        self.speed-=1

    def getSpeed(self):
        return self.speed
    
    def distance_covered(self):
        return self.speed*10
    
    def crash_chance(self):
        crash_chance=self.speed*random.randint(0,101)
        if crash_chance>3000:
            self.speed=0
            return True
        else:
            return False
        
    
class car(vehicle):
    def __init__(self,colour,wheels):
        super().__init__()
        self.colour=colour
        self.wheels=wheels

class bike(vehicle):
    def __init__(self,colour,wheels):
        super().__init__()
        self.colour=colour
        self.wheels=wheels

greenCar=car("Green",4)
redCar=car("Red",4)
blueBike=bike("Blue",2)

def race():
    race=True
    while race==True:
        greenCar.accelerate()
        redCar.accelerate()
        blueBike.accelerate()

        print("green cars distance is ",greenCar.distance_covered())
        print("red cars distance is ",redCar.distance_covered())
        print("blue bikes distance is ",blueBike.distance_covered())

        crashgreen=greenCar.crash_chance()
        crashred=redCar.crash_chance()
        crashblue=blueBike.crash_chance()

        distance_green=greenCar.distance_covered()
        distance_red=redCar.distance_covered()
        distance_blue=blueBike.distance_covered()



        if distance_green==500:
            print("green car has won!!!")
            race=False
        elif distance_red==500:
            print("red car has won!!!")
            race=False
        elif distance_blue==500:
            print("blueBike has won!!!")
            race=False

race()



