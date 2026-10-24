days = int(input())
wins_per_day = 0
loses_per_day = 0
total_wins = 0
total_loses = 0
day_income = 0.0
total_income = 0.0

for _ in range(days):

    while True:
        sport = input()
        if sport == "Finish":
            if wins_per_day > loses_per_day:
                day_income *= 1.10
            total_income += day_income
            total_wins += wins_per_day
            total_loses += loses_per_day
            wins_per_day = 0
            loses_per_day = 0
            day_income = 0.0
            break

        result = input()
        if result == "win":
            wins_per_day += 1
            day_income += 20.00
        elif result == "lose":
            loses_per_day += 1

if total_wins > total_loses:
    total_income *= 1.20
    print(f"You won the tournament! Total raised money: {total_income:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_income:.2f}")
