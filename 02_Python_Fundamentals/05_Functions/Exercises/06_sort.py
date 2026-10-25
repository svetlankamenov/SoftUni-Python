user_input = input().split(" ")
numbers = []

for number in user_input:
    numbers.append(int(number))

numbers = sorted(numbers)
print(numbers)