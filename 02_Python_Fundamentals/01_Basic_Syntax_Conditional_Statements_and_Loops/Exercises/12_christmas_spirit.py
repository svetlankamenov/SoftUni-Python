money_spent = 0
spirit_points = 0

decorations_quantity = int(input())
days_left = int(input())

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        money_spent += decorations_quantity * 2
        spirit_points += 5
    if day % 3 == 0:
        money_spent += decorations_quantity * 8
        spirit_points += 13
    if day % 5 == 0:
        money_spent += decorations_quantity * 15
        spirit_points += 17
        if day % 3 == 0:
            spirit_points += 30
    if day % 10 == 0:
        money_spent += 23
        spirit_points -= 20

if days_left % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")