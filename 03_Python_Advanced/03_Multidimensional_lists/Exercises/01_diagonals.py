matrix = []
primary_diagonal = []
secondary_diagonal = []
sum_of_primary_diagonal = 0
sum_of_secondary_diagonal = 0

n = int(input())

for _ in range(n):
    numbers = [num for num in map(int, input().split(", "))]
    matrix.append(numbers)

for i in range(n):
    sum_of_primary_diagonal += matrix[i][i]
    primary_diagonal.append(matrix[i][i])

    sum_of_secondary_diagonal += matrix[i][n-i-1]
    secondary_diagonal.append(matrix[i][n-i-1])

print(f"Primary diagonal:", end=" ")
print(", ".join(map(str, primary_diagonal)) + f". Sum: {sum_of_primary_diagonal}")
print(f"Secondary diagonal:", end=" ")
print(", ".join(map(str, secondary_diagonal)) + f". Sum: {sum_of_secondary_diagonal}")