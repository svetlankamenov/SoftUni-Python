user_input = input().split(", ")
numbers = list(map(int, user_input))

even_numbers_indices = map(lambda i: i if numbers[i] % 2 == 0 else "no", range(len(numbers)))
even_numbers_indices = list(filter(lambda i: i != "no", even_numbers_indices))

print(even_numbers_indices)