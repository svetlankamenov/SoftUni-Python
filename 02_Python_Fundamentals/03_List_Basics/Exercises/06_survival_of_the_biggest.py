numbers = []

user_input = input().split(" ")
n = int(input())

for i in user_input:
    numbers.append(int(i))

ordered_numbers = sorted(numbers)

for i in range(n):
    numbers.remove(ordered_numbers[i])

print(*numbers, sep=", ")