from collections import deque

matrix = []

rows, cols = map(int, input().split(" "))
snake = deque(list(input()))

for row in range(rows):
    line = ""
    for col in range(cols):
        ch = snake.popleft()
        line +=  ch
        snake.append(ch)

    if row % 2 != 0 and row != 0:
        matrix.append(line[::-1])
    else:
        matrix.append(line)

for row in matrix:
    print(row)