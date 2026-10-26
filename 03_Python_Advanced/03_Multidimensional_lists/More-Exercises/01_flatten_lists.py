matrix = []

numbers = input().split("|")
for line in numbers:
    line = line.strip().split()
    matrix.append(line)

flattened_matrix = []
while matrix:
    flattened_matrix.extend(matrix.pop())

print(" ".join(flattened_matrix))