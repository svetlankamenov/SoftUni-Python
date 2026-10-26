matrix = []

n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split(" ")))
    matrix.append(numbers)

bombs = []
coordinates = input().split(" ")
for i in range(len(coordinates)):
    bombs.append(tuple(map(int, coordinates[i].split(","))))

for bomb in bombs:
    row, col = bomb
    if matrix[row][col] > 0:
        damage = matrix[row][col]
    else:
        continue

    r_start = row - 1
    c_start = col - 1
    r_end = row + 1
    c_end = col + 1

    if row == 0:
        r_start = 0
    elif row == n - 1:
        r_end = n - 1
    if col == 0:
        c_start = 0
    elif col == n - 1:
        c_end = n - 1

    for r in range(r_start, r_end + 1):
        for c in range(c_start, c_end + 1):
            if matrix[r][c] > 0:
                matrix[r][c] -= damage

alive_cells = 0
sum_alive_cells = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            sum_alive_cells += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for row in matrix:
    print(" ".join(map(str, row)))