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
        print("Invalid Choice: ")

    print(f"\n Result \n {number1}  {operator} {number2} = {valor}")

    print("Tank you")


op = 1

while int(op) < 5:
    number1 = input("\n \n Enter Number 1 \n\n")
    number2 = input("enter Number2 \n\n")

    print("\n 1.- Add")
    print("\n 2.- Substract")
    print("\n 3.- Divide")
    print("\n 4.- Multiply")
    print("\n 5.- Exit")
    op = input("\n Choose Operation")

    oper(int(op), int(number1), int(number2))
