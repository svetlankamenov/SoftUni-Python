import math

guests_count = int(input())
budget = float(input())

easter_bread = math.ceil(guests_count / 3)
eggs_count = guests_count * 2

total_expense = (easter_bread * 4.00) + (eggs_count * 0.45)

if total_expense <= budget:
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs_count} eggs.")
    print(f"He has {abs(total_expense-budget):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(total_expense-budget):.2f} lv. more.")