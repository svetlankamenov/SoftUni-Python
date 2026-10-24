sum = float(input())

whole_part = int(sum)
decimal_part = round((sum - whole_part) * 100)
stotinki_coins = 0
leva_coins = 0

if whole_part % 2 == 0:
     leva_coins = whole_part / 2
else:
     whole_part -= 1
     leva_coins = (whole_part / 2) + 1

while decimal_part != 0:
    if decimal_part - 50 >= 0:
        decimal_part -= 50
        stotinki_coins += 1
    elif decimal_part - 20 >= 0:
        decimal_part -= 20
        stotinki_coins += 1
    elif decimal_part - 10 >= 0:
        decimal_part -= 10
        stotinki_coins += 1
    elif decimal_part - 5 >= 0:
        decimal_part -= 5
        stotinki_coins += 1
    elif decimal_part - 2 >= 0:
        decimal_part -= 2
        stotinki_coins += 1
    elif decimal_part - 1 >= 0:
        decimal_part -= 1
        stotinki_coins += 1

print(round(leva_coins + stotinki_coins))