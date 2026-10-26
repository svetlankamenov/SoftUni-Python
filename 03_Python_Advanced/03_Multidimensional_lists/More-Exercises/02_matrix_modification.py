matrix = []

n = int(input())

for _ in range(n):
    matrix.append(list(map(int, input().split())))

while True:
    command = input().split()
    if command[0] == "END":
        for row in matrix:
            print(" ".join(map(str, row)))
        break

    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if 0 <= row < n and 0 <= col < n:
        if command[0] == "Add":
            matrix[row][col] += value
        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")