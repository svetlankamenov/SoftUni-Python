month = input()
overnights = int(input())
apartment_cost = 0.0
studio_cost = 0.0

if month.lower() == "may" or month.lower() == "october":
    studio_cost = overnights * 50.00
    apartment_cost = overnights * 65.00

    if overnights > 7 and overnights < 14:
        studio_cost *= 0.95
    elif overnights > 14:
        studio_cost *= 0.70

    if overnights > 14:
        apartment_cost *= 0.90

    print(f"Apartment: {apartment_cost:.2f} lv.")
    print(f"Studio: {studio_cost:.2f} lv.")

elif month.lower() == "june" or month.lower() == "september":
    studio_cost = overnights * 75.20
    apartment_cost = overnights * 68.70

    if overnights > 14:
        studio_cost *= 0.80
        apartment_cost *= 0.90

    print(f"Apartment: {apartment_cost:.2f} lv.")
    print(f"Studio: {studio_cost:.2f} lv.")

elif month.lower() == "july" or month.lower() == "august":
    studio_cost = overnights * 76.00
    apartment_cost = overnights * 77.00

    if overnights > 14:
        apartment_cost *= 0.90

    print(f"Apartment: {apartment_cost:.2f} lv.")
    print(f"Studio: {studio_cost:.2f} lv.")