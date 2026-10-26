from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split(" ")))

print(max(orders))

for _ in range(len(orders)):
    order = orders.popleft()
    if order <= food_quantity:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    for order in orders:
        print(order, end=" ")