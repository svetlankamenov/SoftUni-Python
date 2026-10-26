from collections import deque

potions = {
    "Brew of Immortality" : 110,
    "Essence of Resilience" : 100,
    "Draught of Wisdom" : 90,
    "Potion of Agility" : 80,
    "Elixir of Strength" : 70
}
crafted_potions = []

substances_quantity = [int(x) for x in input().split(", ")]
crystal_energy_levels = deque(int(x) for x in input().split(", "))

while substances_quantity and crystal_energy_levels and len(crafted_potions) != 5:
    found = False

    substance = substances_quantity.pop()
    crystal = crystal_energy_levels.popleft()
    result = substance + crystal

    for potion, value in potions.items():
        if result == value and potion not in crafted_potions:
            crafted_potions.append(potion)
            found = True
            break

    if not found:
        for potion, value in potions.items():
            if result > value and potion not in crafted_potions:
                crafted_potions.append(potion)
                crystal -= 20
                if crystal > 0:
                    crystal_energy_levels.append(crystal)
                break
        else:
            crystal -= 5
            if crystal > 0:
                crystal_energy_levels.append(crystal)


if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print("Crafted potions: ", end="")
    print(", ".join(crafted_potions))

if substances_quantity:
    substances_quantity.reverse()
    print("Substances: ", end="")
    print(", ".join(map(str, substances_quantity)))

if crystal_energy_levels:
    print("Crystals: ", end="")
    print(", ".join(map(str, crystal_energy_levels)))