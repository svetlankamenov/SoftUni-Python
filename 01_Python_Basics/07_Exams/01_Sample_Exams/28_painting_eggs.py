eggs_size = input()
eggs_colour = input()
lots = int(input())
income = 0.0

if eggs_colour == "Red":
    if eggs_size == "Large":
        income = lots * 16.00
    elif eggs_size == "Medium":
        income = lots * 13.00
    elif eggs_size == "Small":
        income = lots * 9.00

elif eggs_colour == "Green":
    if eggs_size == "Large":
        income = lots * 12.00
    elif eggs_size == "Medium":
        income = lots * 9.00
    elif eggs_size == "Small":
        income = lots * 8.00

elif eggs_colour == "Yellow":
    if eggs_size == "Large":
        income = lots * 9.00
    elif eggs_size == "Medium":
        income = lots * 7.00
    elif eggs_size == "Small":
        income = lots * 5.00

income -= income * 0.35

print(f"{income:.2f} leva.")