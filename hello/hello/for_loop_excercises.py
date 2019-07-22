print("\n ....prime numbers......... \n")


def is_prime(number):
    # check if number is divisible by 2  to numner =1,2,3,4
    if(number < 2):
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


print("is prime? 5 \n")
print(is_prime(5))
print("is prime? 6 \n")
print(is_prime(6))
print("is prime? 7 \n")
print(is_prime(7))


print("\n ....sum up tp......... \n")


def sum_upto_n(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum + i
    return sum


print("Sum up to 3 \n")
print(sum_upto_n(3))

print("Sum up to 5 \n")
print(sum_upto_n(5))

print("Sum up to 10 \n")
print(sum_upto_n(10))


print("\n ....sum of devices ......... \n")


def calculate_sum_of_divisors(number):
    # check if number is divisible by 2  to numner =1,2,3,4
    sum = 0
    if(number < 2):
        return sum
    for divisor in range(1, number+1):
        if number % divisor == 0:
            sum = sum + divisor
    return sum


print(calculate_sum_of_divisors(6))
print(calculate_sum_of_divisors(15))


print("\n .... print a triangle ......... \n")


def print_a_number_triangle(number):
    for j in range(1, number + 1):
        for i in range(1, j+1):
            print(i, end = " ")
        print()


print_a_number_triangle(5)
