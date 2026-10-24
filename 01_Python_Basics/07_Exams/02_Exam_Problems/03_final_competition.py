money_earned = 0.0
donated_money = 0.0

dancers_count = int(input())
score = float(input())
season = input()
place = input()

if place == "Bulgaria":
    money_earned = dancers_count * score
elif place == "Abroad":
    money_earned = dancers_count * score
    money_earned *= 1.50

if season == "summer":
    if place == "Bulgaria":
        money_earned *= 0.95
    elif place == "Abroad":
        money_earned *= 0.90

elif season == "winter":
    if place == "Bulgaria":
        money_earned *= 0.92
    elif place == "Abroad":
        money_earned *= 0.85

donated_money = money_earned * 0.75
money_earned -= donated_money

print(f"Charity - {donated_money:.2f}")
print(f"Money per dancer - {money_earned/dancers_count:.2f}")