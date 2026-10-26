counter_terrorist = {
    "r" : 0,
    "c" : 0,
    "time": 16
}
matrix = []

def move(direction:str, player:dict):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    player["r"] += directions[direction][0]
    player["c"] += directions[direction][1]
    player["time"] -= 1

    if player["r"] < 0:
        player["r"] += 1
    if player["r"] == n:
        player["r"] -= 1
    if player["c"] < 0:
        player["c"] += 1
    if player["c"] == m:
        player["c"] -= 1

    return player

def defuse(player:dict):
    if matrix[player["r"]][player["c"]] != "B":
        player["time"] -= 2
    else:
        player["time"] -= 4

    return player

n, m = tuple(map(int, input().split(", ")))

for i in range(n):
    line = list(input())
    if "C" in line:
        counter_terrorist["r"] = i
        counter_terrorist["c"] = line.index("C")
    matrix.append(line)

while True:
    command = input()
    if command != "defuse":
        counter_terrorist = move(command, counter_terrorist)
    else:
        counter_terrorist = defuse(counter_terrorist)
        if matrix[counter_terrorist["r"]][counter_terrorist["c"]] == "B" and counter_terrorist["time"] >= 0:
            print("Counter-terrorist wins!")
            print(f"Bomb has been defused: {counter_terrorist['time']} second/s remaining.")
            matrix[counter_terrorist["r"]][counter_terrorist["c"]] = "D"
            break
        elif matrix[counter_terrorist["r"]][counter_terrorist["c"]] == "B" and counter_terrorist["time"] < 0:
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print(f"Time needed: {abs(counter_terrorist['time'])} second/s.")
            matrix[counter_terrorist["r"]][counter_terrorist["c"]] = "X"
            break

    if matrix[counter_terrorist["r"]][counter_terrorist["c"]] == "T":
        print("Terrorists win!")
        matrix[counter_terrorist["r"]][counter_terrorist["c"]] = "*"
        break

    if counter_terrorist["time"] <= 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print("Time needed: 0 second/s.")
        break



for line in matrix:
    print("".join(line))