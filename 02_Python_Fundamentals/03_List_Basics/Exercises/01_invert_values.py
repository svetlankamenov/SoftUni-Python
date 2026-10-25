reversed_numbers = []

text = input()
numbers = text.split(" ")

for number in numbers:
    reversed_numbers.append(int(number) * -1)

print(reversed_numbers)