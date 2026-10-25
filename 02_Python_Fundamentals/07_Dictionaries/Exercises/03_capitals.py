countries = input().split(", ")
capitals = input().split(", ")

countries_info = dict(zip(countries, capitals))

for country, capital in countries_info.items():
    print(f"{country} -> {capital}")