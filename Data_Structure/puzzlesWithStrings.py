class puzzle_strings:
    def __init__(self):
        self.animals = ["Cat", "Dog", "Elephant"]
        self.numbers = ["Zeo", "One", "Two", "Three", "Four",
                        "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    def lenght_animals(self):
        return len(self.animals)

    def append_an_animal(self, animal):
        self.animals.append(animal)
        return self.animals

    def remove_an_animal(self, animal):
        self.animals.remove(animal)
        return self.animals

    def return_position_element(self, position):
        return self.animals[position]

    def remove_byIndex_element(self, index):
        del self.animals[index]
        return self.animals

    def extendd_element(self, elem):
        self.animals.extend(elem)
        return self.animals

    def add_many_element(self, elem1, elem2):
        self.animals.extend([elem1, elem2])
        return self.animals

    def add_many_elementV2(self, elem1, elem2):
        self.animals += [elem1, elem2]
        return self.animals

    def not_type_restriction(self, elemint):
        self.animals.append(elemint)
        return self.animals

    def print_element_by_position(self, position):
        return self.animals[position]

    def print_element_by_position_range(self, init, end):
        return self.animals[init:end]

    def print_element_by_position_range_init_cero(self, end):
        return self.animals[:end]

    def print_element_by_position_range_init_End(self, init):
        return self.animals[init:]

    def print_element_by_position_range_everytime(self, init, end, everytime):
        print(f"\n  {self.animals}")
        return self.animals[init:end:everytime]

    def print_element_by_position_range_init_toEnd_everytime(self, everytime):
        print(f"\n {self.animals}")
        return self.animals[::everytime]

    def print_element_by_position_range_init_toEnd_everytime_fromEnd_to_Init(self, everytime):
        print(f"\n {self.animals}")
        return self.animals[::everytime]

    def delete_elements_by_init(self, init):
        print(f"\n {self.animals}")
        del self.animals[init:]
        return self.animals

    def delete_number_by_range(self, init, End):
        print(f"\n {self.numbers}")
        del self.numbers[init:End]
        return self.numbers

    def replace_by_position_range(self, init, End):
        print(f"\n {self.numbers}")
        self.numbers[3:7] = [3, 4, 5, 6]
        return self.numbers

    def list_slicing_by_range(self, Init, End):
        print(f"\n {self.numbers}")
        return self.numbers[Init:End]


puzz = puzzle_strings()

print(f"Lenght: {puzz.lenght_animals()}")
print(puzz.append_an_animal("Fish"))
print(puzz.remove_an_animal("Fish"))
print(f"Print Position: {puzz.return_position_element(1)}")
print(f"Remove element by index {puzz.remove_byIndex_element(1)}")
print(f"Extend Element: {puzz.extendd_element('Cat')}")
print(
    f"Extadd many elements, Giraffe, Horse: {puzz.add_many_element('Giraffe','Horse')}")
print(
    f"Extadd many elements, Jackal, Kangoroo: {puzz.add_many_elementV2('Jackal','Kangoroo')}")
print(f"by position Element [1]: {puzz.print_element_by_position(1)}")
print(
    f"by position by range[1,3]: {puzz.print_element_by_position_range(1,6)}")
print(
    f"by position by range[:3]: {puzz.print_element_by_position_range_init_cero(6)}")
print(
    f" position by range[3:]: {puzz.print_element_by_position_range_init_End(3)}")
print(
    f" position by range by position everytime[3:8:2]: {puzz.print_element_by_position_range_everytime(3,8,2)}")

print(
    f"position by range by everytime[::2]: {puzz.print_element_by_position_range_init_toEnd_everytime(2)}")
print(
    f"position by range by everytime reverse [::-3]: {puzz.print_element_by_position_range_init_toEnd_everytime_fromEnd_to_Init(-3)}")

print(
    f"position by range by everytime[::-3]: {puzz.print_element_by_position_range_init_toEnd_everytime_fromEnd_to_Init(-3)}")

print(f"delete number from init [6:] : {puzz.delete_elements_by_init(6)}")

print(
    f"delete number by range init: End [5:7] : {puzz.delete_number_by_range(5,7)}")

print(
    f"show range [3:4] : {puzz.list_slicing_by_range(2,6)}")
