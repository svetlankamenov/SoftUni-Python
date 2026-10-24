import math

people_count = int(input())
entrance_price = float(input())
deckchair_price = float(input())
umbrella_price = float(input())

umbrella_count = math.ceil(people_count / 2)
deckchair_count = math.ceil(people_count * 0.75)

total_cost = ((people_count * entrance_price) + (deckchair_count * deckchair_price) +
              (umbrella_count * umbrella_price))

print(f"{total_cost:.2f} lv." )