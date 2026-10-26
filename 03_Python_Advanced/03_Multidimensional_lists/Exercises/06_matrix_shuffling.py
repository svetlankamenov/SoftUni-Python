def print_matrix(mtrx: list):
    for row in mtrx:
        print(" ".join(row))

matrix = []

rows, cols = map(int, input().split())

for _ in range(rows):
    data = input().split()
    matrix.append(data)

while True:
    command = input().split(" ")

    if command[0] == "END":
        break
    elif command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = map(int, command[1:])

        if row1 < 0 or row1 > rows or col1 < 0 or col1 > cols:
            print("Invalid input!")
            continue

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        print_matrix(matrix)

    else:
        print("Invalid input!")