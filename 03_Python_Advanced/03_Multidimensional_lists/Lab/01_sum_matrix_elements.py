matrix = []
numbers_sum = 0

rows, cols = list(map(int, input().split(", ")))

for _ in range(rows):
    numbers = list(map(int, input().split(", ")))
    numbers_sum += sum(numbers)
    matrix.append(numbers)

print(numbers_sum)
print(matrix)