gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

fuel_type = input()
fuel_quantity = float(input())
club_card = input()
fuel_cost = 0.0

if club_card.lower() == "yes":
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

if fuel_type.lower() == "gasoline":
    fuel_cost = gasoline_price * fuel_quantity
elif fuel_type.lower() == "diesel":
    fuel_cost = diesel_price * fuel_quantity
elif fuel_type.lower() == "gas":
    fuel_cost = gas_price * fuel_quantity

if fuel_quantity >= 20 and fuel_quantity <= 25:
    fuel_cost *= 0.92
elif fuel_quantity > 25:
    fuel_cost *= 0.90

print(f"{fuel_cost:.2f}")