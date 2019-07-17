'''

 #imprimir mensaje con
msg = "VALUE {0} {1} {2}".format(10, 740, 30)
print(msg, "\n")


# imprimir numero del 1 al 10 con variable
for i in range(1, 10):
    print(i, "\n")

# imprimir la tabla del 5
for i in range(1, 11):
    print(f"5 * {i } = { 8* i }")


# Crear metodo
def print_hello_world_twice():
    print("Hello World")
    print("Hello World")

# Llamar Metodo
print_hello_world_twice()


def myfirst_method():

    $ First variable
    mensaje = "I've Create my first Variable"
    print(mensaje)

    # First Method
    print("first Method")

    # First Loop
    for ft in range(1, 11):
        print(f"I've Create my  {ft} Loop")

    print(f"I'm exited to learn python \n\n")


myfirst_method()

# Method with parameters 
def print_hello_world(no_of_times):

    for h in range(1, no_of_times + 1,):
        print(f"Hello World {h}\n")

        print(f"Cuadrado {h} = {h ** 2}")

    print(no_of_times)


print_hello_world(6)


# print squares of numbers

def print_squares_of_numbers(n):
    for i in range(1, n+1):
        print(f"{i} * {i} = {i*i}")


print_squares_of_numbers(5)

# Method with multiple parameters


def print_string(str="Hello World", no_of_times=5):
    for i in range(1, no_of_times+1):
        print(f"{i}:", str)


print_string("Hello World10", 10)
'''


def print_multiplication_table(table, start, end):
    for i in range(start, end+1):
        print(f" { table } * { i }  = { table * i }")


print_multiplication_table(5, 1, 8)


# Indentention

def method_to_understand_indentation():
    for i in range(1, 11):
        print(i)
        print(i)


method_to_understand_indentation()
