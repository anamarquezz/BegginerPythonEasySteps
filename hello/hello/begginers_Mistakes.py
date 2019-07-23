

#_________Mistakes Shadowing______________
sum([12, 34, 56])

number1 = 10
number2 = 20
sum = number1 + number2 #provoca error al sustituir al metodo que existe con el mismo nombre
sum_ = number1 + number2
print(sum_)
del sum #Eliminar variable con del

# sum([12,34,56])
print(sum([12, 34, 56]))

#_________ Mistakes indentation ______________

i = 3
if(i==3):
#print(i) error
    print(i)
  #print(i) Error



