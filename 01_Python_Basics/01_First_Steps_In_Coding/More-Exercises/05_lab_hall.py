import math
w = float(input())
h = float(input())

h = h * 100
w = w * 100

rows = w / 120
rows = math.floor(rows)
desks = (h - 100) / 70
desks = math.floor(desks)

print(rows * desks - 3)