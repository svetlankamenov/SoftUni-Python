guests_count = int(input())
price_for_guest = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    price_for_guest *= 0.85
elif 15 < guests_count <= 20:
    price_for_guest *= 0.80
elif guests_count > 20:
    price_for_guest *= 0.75

cake_price = budget * 0.10

total_expense = (guests_count * price_for_guest) + cake_price

if total_expense <= budget:
    print(f"It is party time! {abs(total_expense-budget):.2f} leva left.")
else:
    print(f"No party! {abs(total_expense-budget):.2f} leva needed.")