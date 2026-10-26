pacman = {
    "r": 0,
    "c": 0,
    "HP": 100,
    "frozen": False
}
field = []
total_stars = 0

def move(direction:str, p:dict):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    p["r"] += directions[direction][0]
    p["c"] += directions[direction][1]

    if p["r"] < 0:
        p["r"] = n - 1
    elif p["r"] == n:
        p["r"] = 0
    elif p["c"] < 0:
        p["c"] = n - 1
    elif p["c"] == n:
        p["c"] = 0

    return p

n = int(input())
for i in range(n):
    line = list(input())
    total_stars += line.count("*")
    if "P" in line:
        j = line.index("P")
        pacman["r"] = i
        pacman["c"] = j
        line[j] = "-"
    field.append(line)

while True:
    if total_stars == 0:
        print("Pacman wins! All the stars are collected.")
        break
    if pacman["HP"] <= 0:
        print(f"Game over! Pacman last coordinates [{pacman['r']},{pacman['c']}]")
        break

    command = input()
    if command == "end":
        print("Pacman failed to collect all the stars.")
        break

    pacman = move(command, pacman)
    if field[pacman["r"]][pacman["c"]] == "*":
        total_stars -= 1
        field[pacman["r"]][pacman["c"]] = "-"
    elif field[pacman["r"]][pacman["c"]] == "F":
        pacman["frozen"] = True
        field[pacman["r"]][pacman["c"]] = "-"
    elif field[pacman["r"]][pacman["c"]] == "G":
        if pacman["frozen"]:
            pacman["frozen"] = False
        else:
            pacman["HP"] -= 50
        field[pacman["r"]][pacman["c"]] = "-"

field[pacman["r"]][pacman["c"]] = "P"

print(f"Health: {pacman['HP']}")

if total_stars != 0:
    print(f"Uncollected stars: {total_stars}")

for line in field:
    print("".join(line))