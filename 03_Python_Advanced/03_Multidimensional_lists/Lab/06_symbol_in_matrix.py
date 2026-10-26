matrix = []
is_found = False
coordinates = []

rows = int(input())

for _ in range(rows):
    row = list(input())
    matrix.append(row)

symbol = input()

for row in range(rows):
    if is_found:
        break
    for col in range(rows):
        if is_found:
            break
        if symbol == matrix[row][col]:
            coordinates.extend([row, col])
            is_found = True

if is_found:
    print(f"({coordinates[0]}, {coordinates[1]})")
else:
    print(f"{symbol} does not occur in the matrix")