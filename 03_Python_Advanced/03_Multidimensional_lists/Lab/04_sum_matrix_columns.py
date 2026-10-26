matrix = []

rows, cols = map(int, input().split(", "))

for _ in range(rows):
    numbers = list(map(int, input().split(" ")))
    matrix.append(numbers)

for i in range(cols):
    column_sum = 0
    for j in range(rows):
        column_sum += matrix[j][i]
    print(column_sum)