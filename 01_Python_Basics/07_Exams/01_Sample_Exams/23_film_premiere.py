projection_name = input()
cinema_menu = input()
tickets_count = int(input())
total_expense = 0.0

if projection_name == "John Wick":
    if cinema_menu == "Drink":
        total_expense = tickets_count * 12.00
    elif cinema_menu == "Popcorn":
        total_expense = tickets_count * 15.00
    elif cinema_menu == "Menu":
        total_expense = tickets_count * 19.00

elif projection_name == "Star Wars":
    if cinema_menu == "Drink":
        total_expense = tickets_count * 18.00
    elif cinema_menu == "Popcorn":
        total_expense = tickets_count * 25.00
    elif cinema_menu == "Menu":
        total_expense = tickets_count * 30.00

    if tickets_count >= 4:
        total_expense *= 0.70

elif projection_name == "Jumanji":
    if cinema_menu == "Drink":
        total_expense = tickets_count * 9.00
    elif cinema_menu == "Popcorn":
        total_expense = tickets_count * 11.00
    elif cinema_menu == "Menu":
        total_expense = tickets_count * 14.00

    if tickets_count == 2:
        total_expense *= 0.85

print(f"Your bill is {total_expense:.2f} leva.")