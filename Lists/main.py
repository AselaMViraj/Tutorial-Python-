names = ['Asela', 'Madusanka', 'Viraj', 'Kumara']
print(names[1:-1])

# write a program that find the largest number in a list
numbers = input("Enter some random numbers followed by space: ")
list = numbers.split()
max = int(list[0])
for i in range(len(list)):
    list[i] = int(list[i])
    if list[i] > max:
        max = list[i]
print(f"The largest number: {max}")