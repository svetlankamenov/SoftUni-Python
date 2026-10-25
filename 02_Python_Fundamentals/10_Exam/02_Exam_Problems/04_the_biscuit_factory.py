import math

total_biscuit_production = 0

biscuits_per_worker = int(input())
workers_count = int(input())
competing_production = int(input())

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuit_production += math.floor((biscuits_per_worker * workers_count) * 0.75)
    else:
        total_biscuit_production += biscuits_per_worker * workers_count

print(f"You have produced {total_biscuit_production} biscuits for the past month.")

difference_in_production = abs(total_biscuit_production - competing_production)

if total_biscuit_production > competing_production:
    print(f"You produce {difference_in_production/competing_production*100:.2f} percent more biscuits.")
else:
    print(f"You produce {difference_in_production/competing_production*100:.2f} percent less biscuits.")