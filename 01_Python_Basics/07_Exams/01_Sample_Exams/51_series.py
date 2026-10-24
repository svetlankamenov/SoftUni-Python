budget = float(input())
series_count = int(input())
discount = 1.00
total_expenses = 0.0

for _ in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        discount *= 0.50
    elif series_name == "Lucifer":
        discount *= 0.60
    elif series_name == "Protector":
        discount *= 0.70
    elif series_name == "TotalDrama":
        discount *= 0.80
    elif series_name == "Area":
        discount *= 0.90

    total_expenses += series_price * discount
    discount = 1.00

if total_expenses <= budget:
    print(f"You bought all the series and left with {abs(total_expenses-budget):.2f} lv.")
else:
    print(f"You need {abs(total_expenses-budget):.2f} lv. more to buy the series!")