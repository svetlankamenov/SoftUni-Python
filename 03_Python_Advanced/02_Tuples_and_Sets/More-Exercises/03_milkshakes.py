from collections import deque

milkshakes = 0

chocolates = list(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))

while chocolates and milk_cups and milkshakes < 5:

    chocolate = chocolates.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate-5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end="")
    print(", ".join(map(str, chocolates)))
else:
    print("Chocolate: empty")

if milk_cups:
    print("Milk: ", end="")
    print(", ".join(map(str, milk_cups)))
else:
    print("Milk: empty")