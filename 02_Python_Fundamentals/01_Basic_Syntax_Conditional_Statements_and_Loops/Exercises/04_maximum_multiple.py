divisor = int(input())
n = int(input())
largest_integer = 0

for i in range(1, n+1):
    if i % divisor == 0:
        largest_integer = i

print(largest_integer)