matrix = []
sum_of_primary_diagonal = 0
sum_of_secondary_diagonal = 0

n = int(input())

for _ in range(n):
    numbers = [num for num in map(int, input().split(" "))]
    matrix.append(numbers)

for i in range(n):
    sum_of_primary_diagonal += matrix[i][i]
    sum_of_secondary_diagonal += matrix[i][n-i-1]

print(abs(sum_of_primary_diagonal-sum_of_secondary_diagonal))