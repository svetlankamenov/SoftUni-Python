import re

pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)"
total_cost = 0
bought_furniture = []

while True:
    line = input()
    if line == "Purchase":
        print("Bought furniture:")
        for furniture in bought_furniture:
            print(furniture)
        print(f"Total money spend: {total_cost:.2f}")
        break

    purchase = re.match(pattern, line)
    if purchase:
        furniture = purchase.group(1)
        price = float(purchase.group(2))
        count = int(purchase.group(3))
        bought_furniture.append(furniture)
        total_cost += price * count