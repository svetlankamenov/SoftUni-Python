overnight_price = 20
transport_card_price = 1.60
museum_ticket_price = 6

people_count = int(input())
overnights_count = int(input())
transport_card_count = int(input())
museum_tickets_count = int(input())

overnights_expenses = overnights_count * overnight_price
transport_expenses = transport_card_count * transport_card_price
museum_expenses = museum_tickets_count * museum_ticket_price

total_expenses = (overnights_expenses + transport_expenses + museum_expenses) * people_count
total_expenses *= 1.25

print(f"{total_expenses:.2f}")