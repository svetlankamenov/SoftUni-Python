film_name = input()
hall_type = input()
tickets_count = int(input())
income = 0.0

if film_name == "A Star Is Born":
    if hall_type == "normal":
        income = tickets_count * 7.50
    elif hall_type == "luxury":
        income = tickets_count * 10.50
    elif hall_type == "ultra luxury":
        income = tickets_count * 13.50

elif film_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        income = tickets_count * 7.35
    elif hall_type == "luxury":
        income = tickets_count * 9.45
    elif hall_type == "ultra luxury":
        income = tickets_count * 12.75

elif film_name == "Green Book":
    if hall_type == "normal":
        income = tickets_count * 8.15
    elif hall_type == "luxury":
        income = tickets_count * 10.25
    elif hall_type == "ultra luxury":
        income = tickets_count * 13.25

elif film_name == "The Favourite":
    if hall_type == "normal":
        income = tickets_count * 8.75
    elif hall_type == "luxury":
        income = tickets_count * 11.55
    elif hall_type == "ultra luxury":
        income = tickets_count * 13.95

print(f"{film_name} -> {income:.2f} lv.")