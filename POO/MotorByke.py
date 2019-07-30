# MotorBike Encapsulation
class MotorByke:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        if(self.speed - how_much > 0):
            self.speed += how_much
        else:
            print("Get a life")


honda = MotorByke(50)
ducati = MotorByke(250)\

print(honda.speed)
print(ducati.speed)

print("increase")
honda.increase_speed(150)
ducati.increase_speed(25)

print(honda.speed)
print(ducati.speed)


honda.decrease_speed(300)
ducati.decrease_speed(25)

print("decrease")
print(honda.speed)
print(ducati.speed)
