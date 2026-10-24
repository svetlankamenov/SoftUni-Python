import math

sugar_packets = 0
flour_packets = 0
total_sugar_quantity = 0
total_flour_quantity = 0
max_sugar_used = 0
max_flour_used = 0

easter_bread_count = int(input())

for _ in range(easter_bread_count):
    sugar_used = int(input())
    flour_used = int(input())

    total_sugar_quantity += sugar_used
    total_flour_quantity += flour_used

    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used

sugar_packets = math.ceil(total_sugar_quantity / 950)
flour_packets = math.ceil(total_flour_quantity / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")