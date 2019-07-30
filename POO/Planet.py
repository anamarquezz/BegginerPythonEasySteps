class Planet:
    def __init__(self, name="Earth"):
        self.speed = 10  # default value
        self.name = name
        self.distance_from_sun = 10000  # default value


earth = Planet()
print(earth.name, "\n")
print(earth.speed, "\n")
print(earth.distance_from_sun, "\n")
