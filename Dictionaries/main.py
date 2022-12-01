# define a dictionary
customer = {
    "name": "Asela Madusanka",
    "age": 25,
    "is_verified": True
}

# get the values associated with keys
print(customer["name"])

# using get() function
print(customer.get("birthday"))

# update existing value
customer["age"] = 30
print(customer["age"])

# add new key-value pair
customer["birthday"] = "10.21.1997"
print(customer)

# simple exercise
numbers = {"0": "zero", "1": "one", "2": "two",
           "3": "Three", "4": "four", "5": "five",
           "6": "six", "7": "seven", "8": "eight", "9": "nine"
           }

number = input("Phone number: ")
str = ""
for num in number:
    ch = numbers.get(num, "!")
    str += ch + " "
print(str)