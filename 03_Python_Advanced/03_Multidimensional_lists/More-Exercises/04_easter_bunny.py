field = []

bunny = ()
max_eggs = float("-inf")
direction = ""
bunny_path = []

def move_up(r:int, c:int):
    eggs = 0
    path = []

    for r in range(r-1,-1, -1):
        if field[r][c] == "X":
            break
        else:
            eggs += int(field[r][c])
            path.append([r, c])

    return eggs, path

def move_down(r:int, c:int):
    eggs = 0
    path = []

    for r in range(r+1, n):
        if field[r][c] == "X":
            break
        else:
            eggs += int(field[r][c])
            path.append([r, c])

    return eggs, path

def move_left(r:int, c:int):
    eggs = 0
    path = []

    for c in range(c-1, -1, -1):
        if field[r][c] == "X":
            break
        else:
            eggs += int(field[r][c])
            path.append([r, c])

    return eggs, path

def move_right(r:int, c:int):
    eggs = 0
    path = []

    for c in range(c+1, n):
        if field[r][c] == "X":
            break
        else:
            eggs += int(field[r][c])
            path.append([r, c])

    return eggs, path


n = int(input())

for row in range(n):
    line = input().split()
    if "B" in line:
        bunny = (row, line.index("B"))
    field.append(line)

eggs, path = move_up(*bunny)

if eggs > max_eggs:
    max_eggs = eggs
    bunny_path = path
    direction = "up"

eggs, path = move_down(*bunny)

if eggs > max_eggs:
    max_eggs = eggs
    bunny_path = path
    direction = "down"

eggs, path = move_left(*bunny)

if eggs > max_eggs:
    max_eggs = eggs
    bunny_path = path
    direction = "left"

eggs, path = move_right(*bunny)

if eggs > max_eggs:
    max_eggs = eggs
    bunny_path = path
    direction = "right"

print(direction)
for line in bunny_path:
    print(line)
print(max_eggs)