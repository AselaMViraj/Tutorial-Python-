import utils
numbers = input("Enter numbers followed by space: ")
numbers = numbers.split()
print(f'Maximum number= {utils.find_max(numbers)}')
