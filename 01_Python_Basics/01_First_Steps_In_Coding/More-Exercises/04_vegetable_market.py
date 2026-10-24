veg_price = float(input())
fruit_price = float(input())
veg_kg = int(input())
fruit_kg = int(input())

money = (veg_price * veg_kg) + (fruit_price * fruit_kg)
money = money / 1.94
print(f"{money:.2f}")
