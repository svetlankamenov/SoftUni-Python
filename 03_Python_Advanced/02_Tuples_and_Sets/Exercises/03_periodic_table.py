elements = set()

n = int(input())

for _ in range(n):
    line = input().split(" ")
    for element in line:
        elements.add(element)

for element in elements:
    print(element)