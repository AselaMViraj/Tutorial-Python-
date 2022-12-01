# Handling Errors
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Format")
    print("\n")

try:
    age = int(input("Age: "))
    income = int(input("Income: "))
    wealth = income/age
    print(f'Wealth: {wealth}')
except ZeroDivisionError:
    print("Age can not be zero")