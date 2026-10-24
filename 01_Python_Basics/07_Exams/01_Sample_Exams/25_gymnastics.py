score = 0
country = input()
equipment = input()

if country == "Russia":
    if equipment == "ribbon":
        score = 9.100 + 9.400
    elif equipment == "hoop":
        score = 9.300 + 9.800
    elif equipment == "rope":
        score = 9.600 + 9.000

elif country == "Bulgaria":
    if equipment == "ribbon":
        score = 9.600 + 9.400
    elif equipment == "hoop":
        score = 9.550 + 9.750
    elif equipment == "rope":
        score = 9.500 + 9.400

elif country == "Italy":
    if equipment == "ribbon":
        score = 9.200 + 9.500
    elif equipment == "hoop":
        score = 9.450 + 9.350
    elif equipment == "rope":
        score = 9.700 + 9.150

print(f"The team of {country} get {score:.3f} on {equipment}.")
print(f"{100 - (score/20*100):.2f}%")