puzzle_price = 2.60
doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

toys_count = puzzles + dolls + teddy_bears + minions + trucks

earned_money = ((puzzle_price * puzzles) +
              (doll_price * dolls) +
              (teddy_bear_price * teddy_bears) +
              (minion_price * minions) + (truck_price * trucks))

if toys_count >= 50:
    earned_money *= 0.75

rent = earned_money * 0.10
earned_money -= rent

if earned_money >= trip_price:
    print(f"Yes! {abs(earned_money - trip_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(earned_money - trip_price):.2f} lv needed.")