total_cost = 0.0

fruit = input()
set_size = input()
set_count = int(input())

if fruit == "Watermelon":
    if set_size == "small":
        total_cost = set_count * 2 * 56.00
    elif set_size == "big":
        total_cost = set_count * 5 * 28.70

elif fruit == "Mango":
    if set_size == "small":
        total_cost = set_count * 2 * 36.66
    elif set_size == "big":
        total_cost = set_count * 5 * 19.60

elif fruit == "Pineapple":
    if set_size == "small":
        total_cost = set_count * 2 * 42.10
    elif set_size == "big":
        total_cost = set_count * 5 * 24.80

elif fruit == "Raspberry":
    if set_size == "small":
        total_cost = set_count * 2 * 20.00
    elif set_size == "big":
        total_cost = set_count * 5 * 15.20

if 400 <= total_cost <= 1000:
    total_cost *= 0.85
elif total_cost > 1000:
    total_cost *= 0.50

print(f"{total_cost:.2f} lv.")