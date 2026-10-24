import math

magnolia_price = 3.25
hyacinth_price = 4.00
rose_price = 3.50
cactus_price = 8.00

magnolia_num = int(input())
hyacinth_num = int(input())
rose_num = int(input())
cactus_num = int(input())
gift_price = float(input())

income = ((magnolia_price * magnolia_num) +
          (hyacinth_price * hyacinth_num) +
          (rose_price * rose_num) +
          (cactus_price * cactus_num))

income *= 0.95
difference = abs(income - gift_price)

if income >= gift_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")