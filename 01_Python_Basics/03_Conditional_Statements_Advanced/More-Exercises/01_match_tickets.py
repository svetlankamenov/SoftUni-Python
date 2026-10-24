budged = float(input())
ticket = input()
people_count = int(input())
transport_cost = 0.0
ticket_cost = 0.0

if 1 <= people_count <= 4:
    transport_cost = budged * 0.75
elif 5 <= people_count <= 9:
    transport_cost = budged * 0.60
elif 10 <= people_count <= 24:
    transport_cost = budged * 0.50
elif 25 <= people_count <= 49:
    transport_cost = budged * 0.40
else:
    transport_cost = budged * 0.25

budged -= transport_cost

if ticket.lower() == "vip":
    ticket_cost = people_count * 499.99
elif ticket.lower() == "normal":
    ticket_cost = people_count * 249.99

if budged >= ticket_cost:
    print(f"Yes! You have {abs(budged-ticket_cost):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budged-ticket_cost):.2f} leva.")