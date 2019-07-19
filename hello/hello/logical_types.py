def numeric_logical():

    # Condition
    number1 = 10
    number2 = 15
    print(f"\n number1 >  number2 : {number1 > number2}")

    a = 9
    b = 2
    c = 3
    d = 5
    valor = False
    if a + b > c + d:
        valor = True

    print(f"\n....{valor}")

    andatt = True and True
    andatf = True and False
    oroTT = True or True
    oroTF = True or False

    print(
        f"\n ........... \n Logical Operators: \n andatt: {andatt}, \nandatf: {andatf} \n oroTT: {oroTT} \n oroTF: {oroTF}")

    i = 15
    j = 16
    if i % 2 == 0 and j % 2 == 0:
        print("\n \n i and j are even")

    if i % 2 == 0 or j % 2 == 0:
        print("\n \n at least on of i and j are even")

    x = 5
    if not x == 6:
        print("This")
    x = 8
    if not x == 7:
        print("This")

numeric_logical()