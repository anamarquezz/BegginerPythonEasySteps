
try:
    10/0
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")

'''
try:
    10/0
except object:
    # catching classes that do not inherit from BaseException is not allowed
    print("ZeroDivisionError")


'''

try:
    10/0
except BaseException:
    print("BaseException")


#more details
try:
    # 10/0
    sum([1, '1'])
except (ZeroDivisionError, TypeError):
    print("BaseException")


try:
    sum([1, '1'])
except TypeError as error:
    print(error)


print("END")
