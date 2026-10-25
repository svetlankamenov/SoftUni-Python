broken_helmets_count = 0
broken_swords_count = 0
broken_shields_count = 0
broken_armor_count = 0

losts_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for fight in range(1, losts_count+1):
    if fight % 2 == 0:
        broken_helmets_count += 1
    if fight % 3 == 0:
        broken_swords_count += 1
        if fight % 2 == 0:
            broken_shields_count += 1
            if broken_shields_count % 2 == 0:
             broken_armor_count += 1

total_expenses = ((helmet_price * broken_helmets_count) +
                  (sword_price * broken_swords_count) +
                  (shield_price * broken_shields_count) +
                  (armor_price * broken_armor_count))

print(f"Gladiator expenses: {total_expenses:.2f} aureus")