farm_bag = {"shards" : 0, "fragments" : 0, "motes" : 0}
is_obtained = False

while True:
    farm = input().split(" ")
    for i in range(0, len(farm), 2):
        material = farm[i+1].lower()
        quantity = int(farm[i])
        if material in farm_bag:
            farm_bag[material] += quantity
        else:
            farm_bag[material] = quantity

        if farm_bag["shards"] >= 250:
            farm_bag["shards"] -= 250
            print("Shadowmourne obtained!")
            is_obtained = True
            break
        elif farm_bag["fragments"] >= 250:
            farm_bag["fragments"] -= 250
            print("Valanyr obtained!")
            is_obtained = True
            break
        elif farm_bag["motes"] >= 250:
            farm_bag["motes"] -= 250
            print("Dragonwrath obtained!")
            is_obtained = True
            break

    if is_obtained:
        break

for material, quantity in farm_bag.items():
    print(f"{material}: {quantity}")