hall_rent = float(input())

cake_price = hall_rent * 0.20
drinks_price = cake_price - (cake_price * 0.45)
animator_price = hall_rent / 3

budget_needed = hall_rent + cake_price + drinks_price + animator_price
print(f"{budget_needed:.1f}")