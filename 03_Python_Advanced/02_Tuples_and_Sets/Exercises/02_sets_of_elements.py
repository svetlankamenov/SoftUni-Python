first_set = set()
second_set = set()

m, n = map(int, input().split())

for _ in range(m):
    first_set.add(int(input()))

for _ in range(n):
    second_set.add(int(input()))

o = first_set & second_set

for num in o:
    print(num)