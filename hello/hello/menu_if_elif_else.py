def oper(o, number1, number2):
    valor = 0
    operator = "+"
    if o == 1:
        print("\n Add")
        operator = "+"
        valor = int(number1) + int(number2)
    elif o == 2:
        print(f"\n Subst")
        operator = "-"
        valor = int(number1) - int(number2)
    elif o == 3:
        print("\n Divide")
        operator = "/"
        valor = int(number1) / int(number2)
    elif o == 4:
        print("\n Multiply")
        operator = "*"
        valor = int(number1) * int(number2)
    else:
        print("Invalid Choice")

    print(f"\n {number1}  {operator} {number2} = {valor}")


number1 = input("Enter Number 1 \n\n")
number2 = input("enter Number2 \n\n")

print("\n 1.- Add")
print("\n 2.- Substract")
print("\n 3.- Divide")
print("\n 4.- Multiply")
op = input("\n Choose Operation")

oper(int(op), int(number1), int(number2))
