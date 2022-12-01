def find_max(numbers):
    maximum = int(numbers[0])
    for number in numbers:
        number = int(number)
        if number > maximum:
            maximum = number

    return maximum
