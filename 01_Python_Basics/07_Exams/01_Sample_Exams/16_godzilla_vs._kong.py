film_budged = float(input())
statists_count = int(input())
outfit_price = float(input())
outfit_expense = 0.0

decor_expense = film_budged * 0.10

if statists_count > 150:
    outfit_price *= 0.90
    outfit_expense = outfit_price * statists_count
else:
    outfit_expense = outfit_price * statists_count

total_expense = outfit_expense + decor_expense

if film_budged >= total_expense:
    print("Action!")
    print(f"Wingard starts filming with {abs(film_budged-total_expense):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(film_budged-total_expense):.2f} leva more.")