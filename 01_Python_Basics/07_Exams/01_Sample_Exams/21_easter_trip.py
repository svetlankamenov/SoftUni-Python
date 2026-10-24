location = input()
date = input()
overnights = int(input())
total_expense = 0.0

if location == "France":
    if date == "21-23":
        total_expense = overnights * 30.00
    elif date == "24-27":
        total_expense = overnights * 35.00
    elif date == "28-31":
        total_expense = overnights * 40.00

elif location == "Italy":
    if date == "21-23":
        total_expense = overnights * 28.00
    elif date == "24-27":
        total_expense = overnights * 32.00
    elif date == "28-31":
        total_expense = overnights * 39.00

elif location == "Germany":
    if date == "21-23":
        total_expense = overnights * 32.00
    elif date == "24-27":
        total_expense = overnights * 37.00
    elif date == "28-31":
        total_expense = overnights * 43.00

print(f"Easter trip to {location} : {total_expense:.2f} leva.")