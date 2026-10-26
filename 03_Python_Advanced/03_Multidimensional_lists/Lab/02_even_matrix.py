matrix = []

rows = int(input())

for _ in range(rows):
    numbers = [num for num in map(int, input().split(", ")) if num % 2 == 0]
    matrix.append(numbers)

print(matrix)