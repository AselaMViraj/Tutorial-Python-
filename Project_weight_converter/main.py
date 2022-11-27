weight = input("Weight: ")
unit = input("(L)lbs or (K)g: ")

if unit == "L" or unit == "l":
    print(f'You are {int(weight)*2.20462}lbs.')

elif unit == "K" or unit == "k":
    print(f'You are {int(weight) / 2.20462}kg.')

else:
    print("Enter valid symbol")


# better way
weight = input("Weight: ")
unit = input("(L)lbs or (K)g: ")

if unit.upper() == "L":
    print(f'You are {int(weight)*2.20462}lbs.')

elif unit.upper() == "K":
    print(f'You are {int(weight) / 2.20462}kg.')

else:
    print("Enter valid symbol")