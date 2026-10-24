flour_price_per_kilo = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
eggshell_count = int(input())
maya_count = int(input())

sugar_price_per_kilo = flour_price_per_kilo - (flour_price_per_kilo * 0.25)
eggshell_price = flour_price_per_kilo + (flour_price_per_kilo * 0.10)
maya_price = sugar_price_per_kilo - (sugar_price_per_kilo * 0.80)

total_cost = ((flour_kilos * flour_price_per_kilo) +
              (sugar_kilos * sugar_price_per_kilo) +
              (eggshell_count * eggshell_price) +
              (maya_count * maya_price))

print(f"{total_cost:.2f}")