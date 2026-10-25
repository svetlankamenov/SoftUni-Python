numbers = []

factor = int(input())
count = int(input())
number = factor

while len(numbers) < count:
    if number % factor == 0:
        numbers.append(number)
    number += 1

print(numbers)