matrix = []
submatrixes = {}

rows, cols = map(int, input().split(", "))

for _ in range(rows):
    numbers = list(map(int, input().split(", ")))
    matrix.append(numbers)

for row in range(rows-1):
    for col in range(cols-1):
        sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if sum not in submatrixes:
            submatrixes[sum] = [[matrix[row][col], matrix[row][col+1]],
                                [matrix[row+1][col],matrix[row+1][col+1]]]

max_sum = max(submatrixes)

for row in submatrixes[max_sum]:
    print(" ".join(map(str, row)))

print(max_sum)