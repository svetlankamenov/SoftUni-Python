def drive_car(car: str, distance: int, fuel: int, cars_info: dict):
    if cars_info[car]["Fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars_info[car]["Mileage"] += distance
        cars_info[car]["Fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if cars_info[car]["Mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        del cars_info[car]

    return cars_info

def refuel_car(car: str, fuel: int, cars_info: dict):
    cars_info[car]["Fuel"] += fuel
    if cars_info[car]["Fuel"] > 75:
        print(f"{car} refueled with {abs(cars_info[car]['Fuel'] - 75 - fuel)} liters")
        cars_info[car]["Fuel"] = 75
    else:
        print(f"{car} refueled with {fuel} liters")

    return cars_info


def revert_car(car: str, kilometers: int, cars_info: dict):
    cars_info[car]["Mileage"] -= kilometers
    print(f"{car} mileage decreased by {kilometers} kilometers")

    if cars_info[car]["Mileage"] < 10000:
        cars_info[car]["Mileage"] = 10000

    return cars_info

def print_info(cars_info: dict):
    for car in cars_info.keys():
        print(f"{car} -> Mileage: {cars_info[car]['Mileage']} kms, Fuel in the tank: {cars_info[car]['Fuel']} lt.")

cars = {
}

n = int(input())

for _ in range(n):
    car_info = input()
    car_info = car_info.split("|")
    cars[car_info[0]] = {"Mileage" : int(car_info[1]), "Fuel" : int(car_info[2])}

while True:
    command = input()
    if command == "Stop":
        print_info(cars)
        break

    command = command.split(" : ")

    if command[0] == "Drive":
        cars = drive_car(command[1], int(command[2]), int(command[3]), cars)
    elif command[0] == "Refuel":
        cars = refuel_car(command[1], int(command[2]), cars)
    elif command[0] == "Revert":
        cars = revert_car(command[1], int(command[2]), cars)