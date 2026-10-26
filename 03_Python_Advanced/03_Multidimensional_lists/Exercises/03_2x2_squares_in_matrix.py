matrix = []
submatrixes = []

rows, cols = map(int, input().split(" "))

for _ in range(rows):
    line = input().split(" ")
    matrix.append(line)

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            submatrixes.append([[matrix[row][col], matrix[row][col+1]],
                                [matrix[row+1][col],matrix[row+1][col+1]]])

print(len(submatrixes))