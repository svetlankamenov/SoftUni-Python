fuel = input()
fuel_quantity = float(input())

if fuel.lower() == "diesel" or fuel.lower() == "gasoline" or fuel.lower() == "gas":
    if fuel_quantity >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")