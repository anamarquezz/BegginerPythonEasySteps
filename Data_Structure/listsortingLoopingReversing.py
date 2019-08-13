class list_sorting_looping_reversing:
    def __init__(self):
        self.numbers = ["Zeo", "One", "Two", "Three", "Four",
                        "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    def print_numbers(self):
        for num in self.numbers:
            print(f"Number: {num}")

    def print_numbers_in_reverse(self):
        self.numbers.reverse()
        return print(self.numbers)

    def print_numbers_in_reverse_in_forloop(self):
        for num in reversed(self.numbers):
            print(f"Number: {num}")

    def print_numbers_in_sort_way(self):
        self.numbers.sort()
        return print(self.numbers)

    def print_numbers_in_sorted_in_forloop(self):
        for num in sorted(self.numbers):
            print(num)

    def print_numbers_in_sorted_in_forloop_with_key(self):
        for num in sorted(self.numbers, key=len):
            print(num)

    def print_numbers_in_sorted_in_forloop_with_key_with_reverse(self):
        for num in sorted(self.numbers, key=len, reverse=True):
            print(num)


method = list_sorting_looping_reversing()
method.print_numbers()
print("\n reverse: ")
method.print_numbers_in_reverse()

print("\n Reverse: ")
method.print_numbers_in_reverse_in_forloop()
print("\n Sort: ")
method.print_numbers_in_sort_way()
print("\n Sorted loop: ")
method.print_numbers_in_sorted_in_forloop()

print("\n Sorted loop with key: ")
method.print_numbers_in_sorted_in_forloop_with_key()


print("\n Sorted loop with key in reverse: ")
method.print_numbers_in_sorted_in_forloop_with_key_with_reverse()


numbers = ["Zeo", "One", "Two", "Three", "Four",
           "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
print(f"Numbers in reverse:")
numbers.sort(key=len, reverse=False)
print(numbers)
