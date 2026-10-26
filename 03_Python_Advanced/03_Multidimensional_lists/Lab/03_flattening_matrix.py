matrix = []

rows = int(input())

for _ in range(rows):
    numbers = list(map(int, input().split(", ")))
    matrix.append(numbers)

flattened_matrix = []
for row in matrix:
    flattened_matrix.extend(row)

print(flattened_matrix)