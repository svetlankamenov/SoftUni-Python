target_profit = float(input())
accumulated_sum = 0.0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {abs(accumulated_sum-target_profit):.2f} leva more.")
        break

    cocktail_count = int(input())

    profit = len(cocktail_name) * cocktail_count
    if profit % 2 != 0:
        profit *= 0.75

    accumulated_sum += profit

    if accumulated_sum >= target_profit:
        print("Target acquired.")
        break
    profit = 0

print(f"Club income - {accumulated_sum:.2f} leva.")