sum = 0

n = int(input())

for _ in range(n):
    char = input()
    sum += ord(char)

print(f"The sum equals: {sum}")