total_rakiya_quantity = 0.0
total_degrees_per_liter = 0.0

days_count = int(input())

for _ in range(days_count):
    rakiya_quantity = float(input())
    rakiya_degrees = float(input())

    total_rakiya_quantity += rakiya_quantity
    total_degrees_per_liter += rakiya_quantity * rakiya_degrees

mixture_degrees = total_degrees_per_liter/total_rakiya_quantity

print(f"Liter: {total_rakiya_quantity:.2f}")
print(f"Degrees: {mixture_degrees:.2f}")

if mixture_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= mixture_degrees <= 42:
    print("Super!")
elif mixture_degrees >= 42:
    print("Dilution with distilled water!")