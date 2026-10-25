user_input = input().split(" ")
numbers = []

for number in user_input:
    numbers.append(int(number))

print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")