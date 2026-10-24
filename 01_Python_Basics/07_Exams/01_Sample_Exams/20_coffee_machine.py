total_cost = 0.0
drink = input()
sugar = input()
drinks_count = int(input())

if drink == "Espresso":
    if sugar == "Without":
        total_cost = drinks_count * 0.90
        total_cost *= 0.65
    elif sugar == "Normal":
        total_cost = drinks_count * 1.00
    elif sugar == "Extra":
        total_cost = drinks_count * 1.20

    if drinks_count >= 5:
        total_cost *= 0.75

elif drink == "Cappuccino":
    if sugar == "Without":
        total_cost = drinks_count * 1.00
        total_cost *= 0.65
    elif sugar == "Normal":
        total_cost = drinks_count * 1.20
    elif sugar == "Extra":
        total_cost = drinks_count * 1.60

elif drink == "Tea":
    if sugar == "Without":
        total_cost = drinks_count * 0.50
        total_cost *= 0.65
    elif sugar == "Normal":
        total_cost = drinks_count * 0.60
    elif sugar == "Extra":
        total_cost = drinks_count * 0.70

if total_cost > 15.00:
    total_cost *= 0.80

print(f"You bought {drinks_count} cups of {drink} for {total_cost:.2f} lv.")