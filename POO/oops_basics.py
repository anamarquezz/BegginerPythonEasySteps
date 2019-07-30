# MotorBike
class MotorBike:
    pass


honda = MotorBike()
ducati = MotorBike()
honda.speed = 50
ducati.speed = 250
print(honda)
print(ducati)

print(honda.speed)
print(ducati.speed)

honda.speed += 150  # not gut
print(honda.speed)
