class Book:
    def __init__(self, name):
        self.name = name


# Just accept one parameter, if has more than one, takes the last one
the_at_of_computer_programming = Book("The Art of  computer progrmming")
lerning_python = Book("Lerning python")
lerning_restful_services = Book("Lerning restfull Service in 50 steps")

print("\n :", the_at_of_computer_programming.name, "\n")
print("\n :", lerning_python.name, "\n")
print("\n :", lerning_restful_services.name, "\n")
