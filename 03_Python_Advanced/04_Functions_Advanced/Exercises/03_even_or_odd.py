def even_odd(*args):
    def filter_even():
        even_numbers = []
        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
        return even_numbers

    def filter_odd():
        odd_numbers = []
        for number in numbers:
            if number % 2 != 0:
                odd_numbers.append(number)
        return odd_numbers

    command = args[-1]
    numbers = args[:-1]

    if command == 'even':
        return filter_even()
    elif command == 'odd':
        return filter_odd()

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
