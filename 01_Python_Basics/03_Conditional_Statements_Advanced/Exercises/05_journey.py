budged = float(input())
season = input()
destination = ""
place = ""
cost = 0.0

if budged <= 100:
    destination = "Bulgaria"

    if season.lower() == "summer":
        cost = budged * 0.3
        place = "Camp"
    elif season.lower() == "winter":
        cost = budged * 0.7
        place = "Hotel"

elif 100 < budged <= 1000:
    destination = "Balkans"

    if season.lower() == "summer":
        cost = budged * 0.4
        place = "Camp"
    elif season.lower() == "winter":
        cost = budged * 0.8
        place = "Hotel"

elif budged > 1000:
    destination = "Europe"
    place = "Hotel"
    cost = budged * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {cost:.2f}")