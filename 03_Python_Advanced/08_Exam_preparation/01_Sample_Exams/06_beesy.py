matrix = []
bee = ()
bee_energy = 15
total_honey = 0
once_restored = False

def movement(direction: str, energy: int, honey: int, r:int, c:int):
    directions = {
        "up" : (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    r += directions[direction][0]
    c += directions[direction][1]
    energy -= 1

    if r == n:
        r = 0
    elif r < 0:
        r = n - 1
    if c == n:
        c = 0
    elif c < 0:
        c = n - 1

    if matrix[r][c].isdigit():
        honey += int(matrix[r][c])
        matrix[r][c] = "-"

    return (r, c), energy, honey

n = int(input())

for row in range(n):
    line = list(input())
    if "B" in line:
        bee = (row, line.index("B"))
        line[line.index("B")] = "-"

    matrix.append(line)

while True:
    command = input()

    bee, bee_energy, total_honey = movement(command, bee_energy, total_honey, *bee)

    if matrix[bee[0]][bee[1]] == "H":
        if total_honey >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
            break
        else:
            print("Beesy did not manage to collect enough nectar.")
            break
    else:
        if bee_energy == 0 and once_restored == False and total_honey >= 30:
            bee_energy = total_honey - 30
            total_honey = 30
            once_restored = True
            if bee_energy == 0:
                print("This is the end! Beesy ran out of energy.")
                break
        elif bee_energy == 0:
            print("This is the end! Beesy ran out of energy.")
            break

matrix[bee[0]][bee[1]] = "B"
for line in matrix:
    print("".join(line))