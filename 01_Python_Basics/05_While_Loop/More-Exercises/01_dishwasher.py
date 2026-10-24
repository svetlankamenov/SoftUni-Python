detergent_count = int(input())
dishes_count = 0
pots_count = 0
detergent_quantity = detergent_count * 750
pots_flag = 1

while True:
    things = input()

    if not things == "End":
        if pots_flag % 3 != 0:
            things = int(things)
            dishes_count += things
            detergent_quantity -= things * 5
        elif pots_flag % 3 == 0:
            things = int(things)
            pots_count += things
            detergent_quantity -= things * 15
    else:
        print(f"Detergent was enough!")
        print(f"{dishes_count} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {detergent_quantity} ml.")
        break

    if detergent_quantity <= 0:
        print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")
        break

    pots_flag += 1