# state
class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.isOn = False
        self.speed = 0

    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.isOn, self.speed))

    def switch_on(self):
        self.isOn = True
        self.speed = 3

    def switchOff(self):
        self.isOn = False
        self.speed = 0

    def changeSpeed(self, speedp):
        self.speed += speedp


fan = Fan('Manufacter 1', 5, 'green')
print(f"\n {fan}")
fan.switch_on()
print(f'fan.switch_on():  {fan}')
fan.switchOff()
print(f'fan.switchOff(): {fan}')
fan.switch_on()
print(f'fan.switch_on():  {fan}')
fan.changeSpeed(5)
print(f'fan.changeSpeed(5) {fan}')
