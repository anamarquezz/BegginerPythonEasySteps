# while loop excercises


def print_square_upto_limit(limit):
    i = 1
    while i ** 2 < limit:
        print(i*i, end=" ")
        i = i + 1


print_square_upto_limit(30)


def print_cubic_upto_limit(limit):
    i = 1
    print("\n")
    while i ** 3 < limit:
        print(f"{i**3} ", end=" ")
        i = i + 1


print_cubic_upto_limit(80)
