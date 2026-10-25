gathered_plunder = 0.0

days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

for day in range(1, days + 1):
    gathered_plunder += plunder_per_day

    if day % 3 == 0:
        gathered_plunder += plunder_per_day * 0.5
    if day % 5 == 0:
        gathered_plunder *= 0.70

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {gathered_plunder/expected_plunder*100:.2f}% of the plunder.")