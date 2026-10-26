matrix = []

rows, cols = map(int, input().split())

for row in range(rows):
    row_data = []
    for col in range(cols):
        palindrome = chr(97+row) + chr(97+row+col) + chr(97+row)
        row_data.append(palindrome)
    matrix.append(row_data)

for row in matrix:
    print(" ".join(row))