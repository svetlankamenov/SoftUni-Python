colored_eggs = 0
breads = 0

budget = float(input())
flour_price_per_kilo = float(input())
egg_pack_price = flour_price_per_kilo * 0.75
milk_price_per_liter = flour_price_per_kilo * 1.25 / 4

while True:
    if budget - milk_price_per_liter - flour_price_per_kilo - egg_pack_price < 0 :
        print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
    else:

        budget -= (milk_price_per_liter + flour_price_per_kilo + egg_pack_price)
        breads += 1
        colored_eggs += 3
        if breads % 3 == 0:
            colored_eggs -= breads - 2