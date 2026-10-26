field = []
alice_position = ()
tea_bags = 0

def move(direction:str, r:int, c:int, board: list):
    bags = 0

    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1

    if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]):
        return (r, c), board, False, bags

    if board[r][c] == "R":
        board[r][c] = "*"
        return (r, c), board, False, bags

    if board[r][c] not in (".", "*"):
        bags += int(board[r][c])

    board[r][c] = "*"

    return (r, c), board, True, bags

n = int(input())

for i in range(n):
    line = input().split(" ")
    if "A" in line:
        alice_position = (i, line.index("A"))
        line[line.index("A")] = "*"
    field.append(line)

while True:
    movement = input()
    alice_position, field, flag, bags  = move(movement, *alice_position, board=field)
    tea_bags += bags

    if not flag:
        print("Alice didn't make it to the tea party.")
        break
    elif tea_bags >= 10:
        print("She did it! She went to the party.")
        break

for line in field:
    print(" ".join(line))