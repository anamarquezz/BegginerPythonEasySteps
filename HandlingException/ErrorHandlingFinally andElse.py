# Open File / Resource
try:
    # business Login to read
    i = 0
    j = 10/i
    values = [1, 2]
    sum(values)
except TypeError:
    print("TypeErro")
    j = 10
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
else:  # is executed when the exception ist not run
    print("Else")
finally: #executed when exception happens or not
    # close
    print("Finally")


print(j)
print("End")
