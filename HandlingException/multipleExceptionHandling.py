try:
    i = 2  # not hardcode, getting a input form user
    j = 10/i
    list = [1, 2]
    sum(list)
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0

print(j)
print("END")
