movie_budget = float(input())
location = input()
season = input()
days_count = int(input())
filming_cost = 0.0

if location == "Dubai":
    if season == "Winter":
        filming_cost = days_count * 45000
    elif season == "Summer":
        filming_cost = days_count * 40000

    filming_cost *= 0.70

elif location == "Sofia":
    if season == "Winter":
        filming_cost = days_count * 17000
    elif season == "Summer":
        filming_cost = days_count * 12500

    filming_cost *= 1.25

elif location == "London":
    if season == "Winter":
        filming_cost = days_count * 24000
    elif season == "Summer":
        filming_cost = days_count * 20250

if filming_cost <= movie_budget:
    print(f"The budget for the movie is enough! We have {abs(filming_cost-movie_budget):.2f} leva left!")
else:
    print(f"The director needs {abs(filming_cost-movie_budget):.2f} leva more!")