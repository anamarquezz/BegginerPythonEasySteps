from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.numbers = ["Zeo", "One", "Two", "Three", "Four",
                        "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    def __repr__(self):  # print values
        return repr((self.name, self.population, self.area))

    def list_comprehension(self):
        numbers_length_four = []
        for number in self.numbers:
            if len(number) == 4:
                numbers_length_four.append(number)
        print(f"numbers_length_four: {numbers_length_four}")

        numbers_length_four = [number for number in self.numbers]
        print(
            f"\n numbers_length_four = [number for number in numbers] =>  {numbers_length_four}")

        numbers_length_four = [len(number) for number in self.numbers]
        print(
            f"\n numbers_length_four = [len(number) for number in numbers] =>  {numbers_length_four}")

        numbers_length_four = [number.upper() for number in self.numbers]
        print(
            f"\n numbers_length_four = [number.upper() for number in numbers] =>  {numbers_length_four}")

        numbers_length_four = [
            number for number in self.numbers if len(number) == 4]
        print(
            f"\n numbers_length_four = [number for number in numbers if len(number) == 4] =>  {numbers_length_four}")

        values = [3, 6, 9, 1, 4, 15, 6, 3]
        values_even_pares = [value for value in values if value % 2 == 0]
        print(
            f"\n values_even_pares = [value for value in values if value%2 ==0] => {values_even_pares}")

        values_odd_impares = [value for value in values if value % 2 == 1]
        print(
            f"\n values_odd_impares = [value for value in values if value%2 ==1] => {values_odd_impares}")


contry = Country('Mexico', 1200, 100)


countries = [Country('Mexico', 1200, 100),
             Country('Chinmas hueva ca', 1800, 200),
             Country('Usa', 120, 300)]
'''
print(f"print: {countries}")
print(f"print by range: [0:1] {countries[0:1]}")

countries.append(Country("Russia", 80, 900))
print(f"\n print: {countries}")

print("\n sort: ")  # order by population
countries.sort(key=attrgetter('population'))
print(f"\n print: {countries}")

print("\n sort in reverse: ")  # order by population
countries.sort(key=attrgetter('population'))
print(f"\n print: {countries}")
'''
contry.list_comprehension()
