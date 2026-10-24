age = int(input())
whirlpool_price = float(input())
toys_price = int(input())
money = 0.0
toys_count = 0
additional_money = 1

for i in range(1, age + 1):
    if not i % 2 == 0:
        toys_count += 1
    else:
        money += 10.00 * additional_money
        additional_money += 1
        money -= 1.00

money += toys_count * toys_price

if money >= whirlpool_price:
    print(f"Yes! {abs(money - whirlpool_price):.2f}")
else:
    print(f"No! {abs(money - whirlpool_price):.2f}")