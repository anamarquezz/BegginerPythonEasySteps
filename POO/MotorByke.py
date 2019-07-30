# MotorBike Encapsulation
class MotorByke:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        self.speed += how_much


honda = MotorByke(50)
ducati = MotorByke(250)\

print(honda.speed)
print(ducati.speed)

print("increase")
honda.increase_speed(150)
ducati.increase_speed(25)

print(honda.speed)
print(ducati.speed)


honda.decrease_speed(150)
ducati.decrease_speed(25)

print("decrease")
print(honda.speed)
print(ducati.speed)
