class Book:
    def __init__(self, name, copies = 0):
        self.name = name
        self.copies = copies

    def increaseCopies(self, copies):
        self.copies += copies

    def decreaseCopies(self, copies):
        self.copies -= copies


# Just accept one parameter, if has more than one, takes the last one
the_at_of_computer_programming = Book("The Art of  computer progrmming")
lerning_python = Book("Lerning python")
lerning_restful_services = Book("Lerning restfull Service in 50 steps")


print("\n :", the_at_of_computer_programming.name, "\n")
print("\n Copies :", the_at_of_computer_programming.copies, "\n")

print("\n :", lerning_python.name, "\n")
print("\n Copies :", lerning_python.copies, "\n")

print("\n :", lerning_restful_services.name, "\n")
print("\n Copies :", lerning_restful_services.copies, "\n")


the_at_of_computer_programming.increaseCopies(10)
lerning_python.increaseCopies(3)
lerning_restful_services.increaseCopies(5)


print("\n :", the_at_of_computer_programming.name, "\n")
print("\n Copies :", the_at_of_computer_programming.copies, "\n")

print("\n :", lerning_python.name, "\n")
print("\n Copies :", lerning_python.copies, "\n")

print("\n :", lerning_restful_services.name, "\n")
print("\n Copies :", lerning_restful_services.copies, "\n")


the_at_of_computer_programming.decreaseCopies(10)
lerning_python.decreaseCopies(3)
lerning_restful_services.decreaseCopies(5)


print("\n :", the_at_of_computer_programming.name, "\n")
print("\n Copies :", the_at_of_computer_programming.copies, "\n")

print("\n :", lerning_python.name, "\n")
print("\n Copies :", lerning_python.copies, "\n")

print("\n :", lerning_restful_services.name, "\n")
print("\n Copies :", lerning_restful_services.copies, "\n")
