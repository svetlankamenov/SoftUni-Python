numbers = {}
user_input = tuple(map(float, input().split()))

for num in user_input:
    if num not in numbers:
        numbers[num] = user_input.count(num)

for num, count in numbers.items():
    print(f"{num} - {count} times")