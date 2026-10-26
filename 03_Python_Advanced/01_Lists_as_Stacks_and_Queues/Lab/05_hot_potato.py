from collections import deque

kids_names = deque(input().split(" "))
n = int(input())

counter = 0

while len(kids_names) != 1:
    kid = kids_names.popleft()
    counter += 1
    if counter == n:
        print(f"Removed {kid}")
        counter = 0
        continue
    else:
        kids_names.append(kid)

print(f"Last is {kids_names.popleft()}")