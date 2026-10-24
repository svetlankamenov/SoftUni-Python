budged = int(input())
season = input()
fisherman_count = int(input())
cost = 0.0

if season.lower() == "spring":
    cost += 3000
elif season.lower() == "summer" or season.lower() == "autumn":
    cost += 4200
elif season.lower() == "winter":
    cost += 2600

if fisherman_count <= 6:
    cost *= 0.9
elif fisherman_count >= 7 and fisherman_count <= 11:
    cost *= 0.85
elif fisherman_count >= 12:
    cost *= 0.75

if (fisherman_count % 2 == 0) and not (season.lower() == "autumn"):
    cost *= 0.95

if cost <= budged:
    print(f"Yes! You have {abs(cost-budged):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(cost-budged):.2f} leva.")