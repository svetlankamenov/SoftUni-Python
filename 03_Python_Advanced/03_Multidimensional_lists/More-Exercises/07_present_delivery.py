matrix = []
nice_kids = []
given_presents = 0
position = ()

def move(direction: str, r:int, c:int, gifts: int, received: int):
    directions = {
        "up" : (-1, 0),
        "down" : (1, 0),
        "left" : (0, -1),
        "right" : (0, 1)
    }

    new_r = r + directions[direction][0]
    new_c = c + directions[direction][1]

    if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
        return (r, c), gifts, received

    if matrix[new_r][new_c] == "X":
        matrix[new_r][new_c] = "-"
    elif matrix[new_r][new_c] == "V":
        matrix[new_r][new_c] = "-"
        nice_kids.remove((new_r,new_c))
        received += 1
        gifts -= 1
    elif matrix[new_r][new_c] == "C":
        matrix[new_r][new_c] = "-"
        for value in directions.values():
            if matrix[new_r+value[0]][new_c+value[1]] in ("X", "V"):
                if gifts >= 1:
                    if matrix[new_r + value[0]][new_c + value[1]] == "V":
                        nice_kids.remove((new_r + value[0],new_c + value[1]))
                        received += 1
                    matrix[new_r+value[0]][new_c+value[1]] = "-"
                    gifts -= 1
                else:
                    break

    return (new_r, new_c), gifts, received

presents = int(input())
n = int(input())

for row in range(n):
    line = input().split()

    if "S" in line:
       position = (row, line.index("S"))
       line[line.index("S")] = "-"

    for i, char in enumerate(line):
        if char == "V":
            nice_kids.append((row, i))

    matrix.append(line)

while True:
    command = input()
    if command == "Christmas morning":
        break

    position, presents, given_presents = move(command, *position, presents, given_presents)

    if presents == 0:
        if len(nice_kids) > 0:
            print("Santa ran out of presents!")
        break

matrix[position[0]][position[1]] = "S"
for line in matrix:
    print(*line)

if len(nice_kids) > 0:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
else:
    print(f"Good job, Santa! {given_presents} happy nice kid/s.")