temperature = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if 10 <= temperature <= 18:

    if time_of_day.lower() == "morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif 18 < temperature <= 24:

    if time_of_day.lower() == "morning":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif temperature >= 25:

    if time_of_day.lower() == "morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

    elif time_of_day.lower() == "evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
