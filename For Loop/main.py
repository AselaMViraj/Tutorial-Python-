# simple for loop
for item in "Python":
    print(item)

# for loop with list
for item in ['Asela', 'Madusanka', 'Viraj']:
    print(item)


# for loop with range function
for item in range(1, 11, 2):
    print(item)

# simple example problme
prices = [10, 20, 30, 40, 50]
sum = 0
for price in prices:
    sum = sum + price

print(f'Total price = ${sum}')