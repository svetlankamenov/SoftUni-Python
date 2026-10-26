matrix = []
max_sum = float("-inf")
max_matrix = []

rows, cols = map(int, input().split(" "))

for _ in range(rows):
    numbers = list(map(int, input().split(" ")))
    matrix.append(numbers)

for row in range(rows-2):
    for col in range(cols-2):
        if (matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] +
               matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] +
               matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]) > max_sum:
            max_sum = (matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] +
               matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] +
               matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2])
            max_matrix = [[matrix[row][col],matrix[row][col+1], matrix[row][col+2]],
               [matrix[row+1][col],matrix[row+1][col+1], matrix[row+1][col+2]],
               [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(" ".join(map(str, row)))