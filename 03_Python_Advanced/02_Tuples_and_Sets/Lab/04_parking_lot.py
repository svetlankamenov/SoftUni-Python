parking = set()

n = int(input())

for _ in range(n):
    command, car_number = input().split(", ")
    if command == "IN":
        parking.add(car_number)
    elif command == "OUT":
        if car_number in parking:
            parking.remove(car_number)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")