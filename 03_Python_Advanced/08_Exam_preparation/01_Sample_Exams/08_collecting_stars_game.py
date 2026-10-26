matrix = []
win = False
player = {
    "r" : 0,
    "c" : 0,
    "collected_stars" : 2
}

n = int(input())

def move(direction: str, p: dict):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    p["r"] += directions[direction][0]
    p["c"] += directions[direction][1]

    if p["r"] < 0 or p["c"] < 0 or p["r"] == n  or p["c"] == n:
        p["r"] = 0
        p["c"] = 0

    if matrix[p["r"]][p["c"]] == "*":
        player["collected_stars"] += 1
        matrix[p["r"]][p["c"]] = "."
    elif matrix[p["r"]][p["c"]] == "#":
        player["collected_stars"] -= 1
        p["r"] -= directions[direction][0]
        p["c"] -= directions[direction][1]

    return p

for i in range(n):
    line = input().split()
    if "P" in line:
        player["r"] = i
        player["c"] = line.index("P")
        line[line.index("P")] = "."
    matrix.append(line)

while True:
    command = input()
    player = move(command, player)

    if player["collected_stars"] == 0:
        win = False
        break
    elif player["collected_stars"] == 10:
        win = True
        break

matrix[player["r"]][player["c"]] = "P"

if win:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player['r']}, {player['c']}]")
for line in matrix:
    print(" ".join(line))