possible_moves = [(-1,-2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
knights = {}
board = []
removed_knights = 0

def check_board(b: list, k: dict):
    for row in range(n):
        for col in range(n):
            if b[row][col] == "K":
                for r, c in possible_moves:
                    new_row = row + r
                    new_col = col + c

                    if not (0 <= new_row < n) or not (0 <= new_col < n):
                        continue

                    if b[new_row][new_col] == "K":
                        if (row, col) not in k:
                            k[(row, col)] = 1
                        else:
                            k[(row, col)] += 1

    return b, k

n = int(input())
for _ in range(n):
    board.append(list(input()))

board, knights = check_board(board, knights)

while knights:
    max_knight = max(knights, key=knights.get)

    if knights[max_knight] > 1:
        r, c = max_knight
    else:
        r, c = min(knights)

    board[r][c] = "0"
    removed_knights += 1
    knights.clear()
    board, knights = check_board(board, knights)

print(removed_knights)