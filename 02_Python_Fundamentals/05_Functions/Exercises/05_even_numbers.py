def find_even_numbers(number: int):
    if number % 2 == 0:
        return True

sequence_of_numbers = input().split(" ")
numbers = []

for number in sequence_of_numbers:
    numbers.append(int(number))

even_numbers = filter(find_even_numbers, numbers)
print(list(even_numbers))