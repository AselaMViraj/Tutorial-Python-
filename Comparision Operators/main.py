name = input("Enter your name: ")
max = 50
min = 3

if len(name) < min:
    print("Name must be at least 3 characters.")

elif len(name) > max:
    print("Name must be maximum of 50 characters.")

else:
    print("Looking good.")
