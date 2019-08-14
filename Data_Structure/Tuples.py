class Tuples_data_:
    def __init__(self):
        self.algo = "adasd"

    def create_ranga(self):
        return 'Ranga', 1981, 'India'


l_set = Tuples_data_()
ranga = l_set.create_ranga()
print(f"\n\n {ranga}")
print(f"{type(ranga)}")

print(f"\n\n name, year, country = ranga")
name, year, country = ranga
print(ranga)

print(f"\n name:{name}, \n year:{year}, \n country:{country} ")

print(f"\n\nlen(ranga) {len(ranga)}")
print(f" ranga[0] => {ranga[0]}")
print(f" ranga[1] => {ranga[1]}")
print(f" ranga[2] => {ranga[2]}")  # tupples cant not change unmutable
person = 'Ranga', 5, 'India'
print(f"\n\n type(person) => {type(person)}")
name, age, country = person
print("name,age,country = person")
print(person)
print(f"\n name:{name}, \n age:{age}, \n country:{country} ")
print(f"\n\nx = 0 ")
x = 0
print(f"y = 1")
y = 1
print(f"x, y = 0, 1 => x:{x} y:{y}")
x, y = 0, 1
x, y = y, x
print(f"x, y = y, x  => x:{x} y:{y} ")

print(f"\n\n x = (0)")
x = (0)
print(f"type(x) => {type(x)} ")
print(f"x = (0,) ")
x = (0,)
print(f"x = 1,")
x = 1,
print(f"type(x) => {type(x)}")
