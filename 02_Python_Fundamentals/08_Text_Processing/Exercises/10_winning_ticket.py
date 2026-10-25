def check_ticket(ticket: str):
    unique_symbols = ['@', '#', '$', '^']
    flag = False
    first_half = ticket[:10]
    second_half = ticket[10:]

    for symbol in unique_symbols:
        for i in range(10, 5, -1):
            if (symbol * i) in first_half and (symbol * i) in second_half:
                flag = True
                symbol_count = i
                winning_symbol = symbol
            if flag:
                break
        if flag:
            break

    if flag:
        if symbol_count != 10:
            print(f'ticket "{ticket}" - {symbol_count}{winning_symbol}')
        else:
            print(f'ticket "{ticket}" - {symbol_count}{winning_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')

tickets = input().split(",")
tickets = [ticket.strip() for ticket in tickets]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        check_ticket(ticket)