film_budged = float(input())
statists_count = int(input())
clothes_price = float(input())

film_decor = film_budged * 0.10

if statists_count > 150:
    clothes_price *= 0.90

film_cost = (statists_count * clothes_price) + film_decor

if film_cost <= film_budged:
    print("Action!")
    print(f"Wingard starts filming with {film_budged - film_cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {film_cost - film_budged:.2f} leva more.")