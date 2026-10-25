numbers = []

user_input = input().split(" ")
for i in user_input:
    numbers.append(abs(float(i)))

print(numbers)