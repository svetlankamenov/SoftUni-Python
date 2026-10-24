annual_fee = int(input())

basketball_shoes = annual_fee - (annual_fee * 0.4)
basketball_outfit = basketball_shoes - (basketball_shoes * 0.2)
ball_price = basketball_outfit / 4
basketball_accessories = ball_price / 5

total_expenses = (annual_fee + basketball_shoes + basketball_outfit +
                  ball_price + basketball_accessories)

print(f"{total_expenses:.2f}")