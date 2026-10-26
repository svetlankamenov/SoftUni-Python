maze = []
player = {
    "r": 0,
    "c": 0,
    "HP": 100
}

def move(direction:str, p: dict):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    p["r"] += directions[direction][0]
    p["c"] += directions[direction][1]

    if p["r"] < 0:
        p["r"] = 0
    elif p["r"] == n:
        p["r"] = n - 1
    elif p["c"] < 0:
        p["c"] = 0
    elif p["c"] == n:
        p["c"] = n - 1

    return p

n = int(input())
for i in range(n):
    line = list(input())
    if "P" in line:
        j = line.index("P")
        player["r"] = i
        player["c"] = j
        line[j] = "-"
    maze.append(line)

while True:
    if player["HP"] <= 0:
        print("Player is dead. Maze over!")
        break

    command = input()
    player = move(command, player)

    if maze[player["r"]][player["c"]] == "M":
        player["HP"] -= 40
        if player["HP"] > 0:
            maze[player["r"]][player["c"]] = "-"
        else:
            player["HP"] = 0
    elif maze[player["r"]][player["c"]] == "H":
        player["HP"] += 15
        if player["HP"] > 100:
            player["HP"] = 100
        maze[player["r"]][player["c"]] = "-"
    elif maze[player["r"]][player["c"]] == "X":
        print("Player escaped the maze. Danger passed!")
        break

print(f"Player's health: {player['HP']} units")
maze[player["r"]][player["c"]] = "P"
for line in maze:
    print("".join(line))