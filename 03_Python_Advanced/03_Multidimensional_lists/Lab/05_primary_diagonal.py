matrix = []
sum = 0

rows = int(input())

for i in range(rows):
    numbers = list(map(int, input().split(" ")))
    matrix.append(numbers)
    sum += matrix[i][i]

print(sum)