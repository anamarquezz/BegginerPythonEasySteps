class list_sorting_looping_reversing:
    def __init__(self):
        self.numbers = ["Zeo", "One", "Two", "Three", "Four",
                        "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    def print_numbers(self):
        for num in self.numbers:
            print(f"Number: {num}")

    def print_numbers_in_reverse(self):
        reverse_num = reversed(self.numbers)
        print("Reverse Numbers")
        for num in reverse_num:
            print(f"Number: {num}")

    def print_numbers_in_sort_way(self):
        print(f"Sort: {self.numbers.sort()}")

    def print_forloop(self):
        for num in sorted(self.numbers):
            print(num)


method = list_sorting_looping_reversing()
method.print_numbers()
print("\n \n")
method.print_numbers_in_reverse()
print("\n")
method.print_numbers_in_sort_way()
print("\n")
method.print_forloop()
