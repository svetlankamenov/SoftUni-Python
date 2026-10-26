matrix = []
targets_info = []
position = ()
removed_targets = []

def move(direction:str, steps:int, r:int, c:int):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    new_row = r + directions[direction][0] * steps
    new_col = c + directions[direction][1] * steps

    if 0 <= new_row < 5 and 0 <= new_col < 5 and matrix[new_row][new_col] == ".":
        return new_row, new_col

    return r, c

def shoot(direction:str, r:int, c:int):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    new_row = r
    new_col = c

    while True:
        new_row += directions[direction][0]
        new_col += directions[direction][1]

        if new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4:
            break

        if matrix[new_row][new_col] == "x":
            removed_targets.append([new_row, new_col])
            targets_info.remove([new_row, new_col])
            matrix[new_row][new_col] = "."
            break

for i in range(5):
    line = input().split(" ")
    if "A" in line:
        position = (i, line.index("A"))
        line[line.index("A")] = "."
    for j, char in enumerate(line):
        if char == "x":
            targets_info.append([i, j])

    matrix.append(line)

n = int(input())

for _ in range(n):
    command = input().split(" ")
    if command[0] == "move":
        position = move(command[1], int(command[2]), *position)
    elif command[0] == "shoot":
        shoot(command[1], *position)

    if len(targets_info) == 0:
        print(f"Training completed! All {len(removed_targets)} targets hit.")
        break

if len(targets_info) != 0:
    print(f"Training not completed! {len(targets_info)} targets left.")
for target in removed_targets:
    print(target)