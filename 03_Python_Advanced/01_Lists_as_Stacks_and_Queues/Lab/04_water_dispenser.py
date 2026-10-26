from collections import deque

queue = deque()

water_quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break

    queue.append(name)

while True:
    command = input()
    if command == "End":
        print(f"{water_quantity} liters left")
        break

    command = command.split(" ")

    if command[0] == "refill":
        water_quantity += int(command[1])

    elif command[0].isdigit():
        if int(command[0]) <= water_quantity:
            print(f"{queue.popleft()} got water")
            water_quantity -= int(command[0])
        else:
            print(f"{queue.popleft()} must wait")