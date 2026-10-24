championship_stage = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()
ticket_price = 0

if championship_stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = ticket_count * 55.50
    elif ticket_type == "Premium":
        ticket_price = ticket_count * 105.20
    elif ticket_type == "VIP":
        ticket_price = ticket_count * 118.90

elif championship_stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = ticket_count * 75.88
    elif ticket_type == "Premium":
        ticket_price = ticket_count * 125.22
    elif ticket_type == "VIP":
        ticket_price = ticket_count * 300.40

elif championship_stage == "Final":
    if ticket_type == "Standard":
        ticket_price = ticket_count * 110.10
    elif ticket_type == "Premium":
        ticket_price = ticket_count * 160.66
    elif ticket_type == "VIP":
        ticket_price = ticket_count * 400.00

if 2500 < ticket_price < 4000:
    ticket_price *= 0.90
elif ticket_price >= 4000:
    ticket_price *= 0.75
    trophy_picture = "N"

if trophy_picture == "Y":
    ticket_price += ticket_count * 40.00

print(f"{ticket_price:.2f}")