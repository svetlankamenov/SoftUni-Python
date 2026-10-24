days = int(input())
room_type = input()
rate = input()
cost = 0.0

if room_type.lower() == "room for one person":
    cost = (days - 1) * 18.00

elif room_type.lower() == "apartment":
    cost = (days - 1) * 25.00

    if days < 10:
        cost *= 0.70
    elif 10 <= days <= 15:
        cost *= 0.65
    else:
        cost *= 0.50

elif room_type.lower() == "president apartment":
    cost = (days - 1) * 35.00

    if days < 10:
        cost *= 0.9
    elif 10 <= days <= 15:
        cost *= 0.85
    else:
        cost *= 0.80

if rate == "positive":
    cost = cost + (cost * 0.25)
elif rate == "negative":
    cost *= 0.90

print(f"{cost:.2f}")