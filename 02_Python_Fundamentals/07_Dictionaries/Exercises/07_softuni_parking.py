parking_info = {}

n = int(input())

for _ in range(n):
    line = input().split(" ")

    if line[0] == "register":
        command = line[0]
        username = line[1]
        car_number = line[2]
    elif line[0] == "unregister":
        command = line[0]
        username = line[1]

    if command == "register":
        if username not in parking_info:
            parking_info[username] = car_number
            print(f"{username} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")
    elif command == "unregister":
        if username not in parking_info:
            print(f"ERROR: user {username} not found")
        else:
            del parking_info[username]
            print(f"{username} unregistered successfully")

for username, car_number in parking_info.items():
    print(f"{username} => {car_number}")