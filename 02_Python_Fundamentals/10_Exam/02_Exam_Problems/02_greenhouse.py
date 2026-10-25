green_house = input().split(" & ")

while True:
    command = input()
    if command == "Collect!":
        green_house_collection = " | ".join(green_house)
        print(green_house_collection)
        break

    command = command.split(" ")

    if command[0] == "Plant":
        if command[1] not in green_house:
            green_house.insert(0, command[1])
    elif command[0] == "Transplant":
        if command[1] in green_house:
            green_house.remove(command[1])
            green_house.append(command[1])
    elif command[0] == "Replace":
        index_1 = int(command[1])
        index_2 = int(command[2])
        if 0 <= index_1 < len(green_house) and  0 <= index_2 < len(green_house):
            green_house[index_1], green_house[index_2] = green_house[index_2], green_house[index_1]
    elif command[0] == "Uproot":
        if command[1] in green_house:
            green_house.remove(command[1])