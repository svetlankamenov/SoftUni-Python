n = int(input())
average = 0.0

for _ in range(n):
    number = int(input())
    average += number

print(f"{average / n:.2f}")