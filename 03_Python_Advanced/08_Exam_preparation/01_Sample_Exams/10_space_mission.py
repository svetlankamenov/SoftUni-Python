matrix = []
spaceship = {
    "r" : 0,
    "c" : 0,
    "fuel" : 100,
    "lost" : False
}

def move(direction: str, ship: dict):
    directions = {
        "up" : (-1, 0),
        "down" : (1, 0),
        "left" : (0, -1),
        "right" : (0, 1)
    }

    ship["r"] += directions[direction][0]
    ship["c"] += directions[direction][1]
    ship["fuel"] -= 5

    if ship["r"] < 0:
        ship["r"] = 0
        ship["lost"] = True
    elif ship["r"] == n:
        ship["r"] = n - 1
        ship["lost"] = True
    elif ship["c"] < 0:
        ship["c"] = 0
        ship["lost"] = True
    elif ship["c"] == n:
        ship["c"] = n - 1
        ship["lost"] = True

    return ship

n = int(input())
for i in range(n):
    line = input().split()
    if "S" in line:
        j = line.index("S")
        spaceship["r"] = i
        spaceship["c"] = j
        line[j] = "."
    matrix.append(line)

while True:
    if spaceship["fuel"] < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

    command = input()
    spaceship = move(command, spaceship)

    if matrix[spaceship["r"]][spaceship["c"]] == "R":
        spaceship["fuel"] += 10
        if spaceship["fuel"] > 100:
            spaceship["fuel"] = 100
    elif matrix[spaceship["r"]][spaceship["c"]] == "M":
        spaceship["fuel"] -= 5
        matrix[spaceship["r"]][spaceship["c"]] = "."
    elif spaceship["lost"]:
        print("Mission failed! The spaceship was lost in space.")
        break
    elif matrix[spaceship["r"]][spaceship["c"]] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {spaceship['fuel']} resources left.")
        break

if matrix[spaceship["r"]][spaceship["c"]] == "P":
    for line in matrix:
        print(" ".join(line))
else:
    matrix[spaceship["r"]][spaceship["c"]] = "S"
    for line in matrix:
        print(" ".join(line))