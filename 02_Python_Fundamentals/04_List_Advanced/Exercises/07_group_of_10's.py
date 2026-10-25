numbers = input().split(", ")
numbers = list(map(int, numbers))

boundary = 10

while len(numbers) >= 1:
    group = [age for age in numbers if age <= boundary]
    for age in group:
        numbers.remove(age)
    print(f"Group of {boundary}'s: {group}")
    boundary += 10