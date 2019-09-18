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
    j = 10
except:
    print("OtherError")
    j = 5
else:  # is executed when the exception ist not run, ist not allowed if there is not except,
    print("Else")
finally:  # executed when exception happens or not, Ist allowed even if there is no except
    # close
    print("Finally")


print(j)
print("End")
