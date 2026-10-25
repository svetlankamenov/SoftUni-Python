numbers = []

user_input = input().split(" ")

for number in user_input:
    numbers.append(round(float(number)))

print(numbers)