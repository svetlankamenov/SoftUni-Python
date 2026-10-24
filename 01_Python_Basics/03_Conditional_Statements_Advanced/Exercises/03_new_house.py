rose_price = 5.00
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50

flowers = input()
flowers_quantity = int(input())
budget = int(input())
cost = 0.0

if flowers.lower() == "roses":
    if flowers_quantity > 80:
        cost = rose_price * flowers_quantity * 0.90
    else:
        cost = rose_price * flowers_quantity

elif flowers.lower() == "dahlias":
    if flowers_quantity > 90:
        cost = dahlia_price * flowers_quantity * 0.85
    else:
        cost = dahlia_price * flowers_quantity

elif flowers.lower() == "tulips":
    if flowers_quantity > 80:
        cost = tulip_price * flowers_quantity * 0.85
    else:
        cost = tulip_price * flowers_quantity

elif flowers.lower() == "narcissus":
    if flowers_quantity < 120:
        cost = narcissus_price * flowers_quantity * 1.15
    else:
        cost = narcissus_price * flowers_quantity

elif flowers.lower() == "gladiolus":
    if flowers_quantity < 80:
        cost = gladiolus_price * flowers_quantity * 1.20
    else:
        cost = gladiolus_price * flowers_quantity

if cost <= budget:
    print(f"Hey, you have a great garden with {flowers_quantity} {flowers} and {abs(cost-budget):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(cost-budget):.2f} leva more.")