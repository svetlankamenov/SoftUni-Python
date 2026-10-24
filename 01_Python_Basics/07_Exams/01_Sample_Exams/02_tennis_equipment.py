import math

tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_count = int(input())
sneakers_price = tennis_racket_price / 6

equipment_price = (tennis_racket_count * tennis_racket_price
                    + sneakers_price * sneakers_count) * 0.2

total_cost = ((tennis_racket_count * tennis_racket_price) +
              (sneakers_count * sneakers_price) + equipment_price)

print(f"Price to be paid by Djokovic {math.floor(total_cost / 8)}")
print(f"Price to be paid by sponsors {math.ceil(total_cost * 7 / 8)}")