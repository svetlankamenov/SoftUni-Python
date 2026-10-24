family_budget = float(input())
overnights_count = int(input())
overnights_price = float(input())
additional_expenses = int(input())
overnight_discount = 1

if overnights_count > 7:
    overnight_discount = 0.95

total_expenses = ((overnights_count * overnights_price * overnight_discount) +
                  (family_budget * additional_expenses/100))

if total_expenses <= family_budget:
    print(f"Ivanovi will be left with {abs(total_expenses-family_budget):.2f} leva after vacation.")
else:
    print(f"{abs(total_expenses-family_budget):.2f} leva needed.")