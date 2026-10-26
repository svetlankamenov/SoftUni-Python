from collections import deque

supermarket = deque()

while True:
    name = input()
    if name == "End":
        print(f"{len(supermarket)} people remaining.")
        break
    if name == "Paid":
        while len(supermarket) != 0:
            print(supermarket.popleft())
        continue

    supermarket.append(name)
