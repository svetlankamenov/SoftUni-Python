import math

vineyard = int(input())
grapes_per_sqm = float(input())
wine_for_sale = int(input())
workers = int(input())

produced_wine = (vineyard * 0.4) * grapes_per_sqm / 2.5
difference = abs(produced_wine - wine_for_sale)

if produced_wine < wine_for_sale:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(difference/workers)} liters per person.")