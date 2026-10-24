tshirt_price = float(input())
target_sum = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = 2 * (tshirt_price + shorts_price)

total_sum = tshirt_price + shorts_price + socks_price + shoes_price
total_sum *= 0.85

if total_sum >= target_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {abs(total_sum-target_sum):.2f} lv. more.")