# printing coordinates
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')


# challenge(without using multiplication of strings)

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    str = ''
    for n in range(i):
        str += 'x'
    print(str)
