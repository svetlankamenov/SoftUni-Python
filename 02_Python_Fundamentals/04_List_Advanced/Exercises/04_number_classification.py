numbers_collection = input().split(", ")
numbers_collection = list(map(int, numbers_collection))

positive_numbers = [number for number in numbers_collection if number >= 0]
negative_numbers = [number for number in numbers_collection if number < 0]
even_numbers = [number for number in numbers_collection if number % 2 == 0]
odd_numbers = [number for number in numbers_collection if number % 2 != 0]

print(f"Positive:", ", ".join(str(x) for x in positive_numbers))
print(f"Negative:", ", ".join(str(x) for x in negative_numbers))
print(f"Even:", ", ".join(str(x) for x in even_numbers))
print(f"Odd:", ", ".join(str(x) for x in odd_numbers))