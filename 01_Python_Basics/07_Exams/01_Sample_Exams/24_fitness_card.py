price = 0.0

available_amount = float(input())
gender = input()
age = int(input())
sport = input()

if gender == "m":
    if sport == "Gym":
        price = 42.00
    elif sport == "Boxing":
        price = 41.00
    elif sport == "Yoga":
        price = 45.00
    elif sport == "Zumba":
        price = 34.00
    elif sport == "Dances":
        price = 51.00
    elif sport == "Pilates":
        price = 39.00

elif gender == "f":
    if sport == "Gym":
        price = 35.00
    elif sport == "Boxing":
        price = 37.00
    elif sport == "Yoga":
        price = 42.00
    elif sport == "Zumba":
        price = 31.00
    elif sport == "Dances":
        price = 53.00
    elif sport == "Pilates":
        price = 37.00

if age <= 19:
    price *= 0.80

if price <= available_amount:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(price-available_amount):.2f} more.")