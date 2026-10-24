hall_price = int(input())

oscar_price = hall_price - (hall_price * 0.3)
catering_price = oscar_price - (oscar_price * 0.15)
sound_price = catering_price / 2

total_cost = hall_price + oscar_price + catering_price + sound_price
print(f"{total_cost:.2f}")