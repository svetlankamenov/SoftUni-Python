capsule_price = 0.0
days = 0
capsules_per_day = 0
current_price = 0.0
total_price = 0.0

orders_count = int(input())

for _ in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if (not 0.01 <= capsule_price <= 100.00 or not 1 <= days <= 31
        or not 1 <= capsules_per_day <= 2000):
        continue

    current_price = capsule_price * days * capsules_per_day
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")