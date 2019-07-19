#Numeric data Types
def numeric_data_types():

    number = 5
    print("\nNumeric",  type(number))

    flotant = 5.5
    print("\n Numeric ", type(flotant))

    increment= 1
    increment += 1
    print("\n Increment: {0} ".format(increment))

    decrement = 2
    decrement -= -1
    print("\n Decrement {0}".format(decrement))

    floatnum = 2.5
    floatnum2 = 5
    print(f"float subs {floatnum} / {floatnum2} = {floatnum / floatnum2}")
    print("\n Float sin decimal subs".format(floatnum // floatnum2))

    poww = 5
    poww2 = 2
    print(f" \n pow con  ** {poww} * {poww2} = { poww ** poww2 }")
    print(f"\n pow con  pow(n,n): { pow(poww,poww2) }")

    intfloat = 5.6
    print(f"\n {intfloat} = int Float: con int() ", int(intfloat))

    intfloatround = 5.6
    print(f"\n Int floar rounded: {intfloatround} con round()", round(intfloatround))

    boolean = False
    print(f"Boolean: {boolean}")


numeric_data_types()
