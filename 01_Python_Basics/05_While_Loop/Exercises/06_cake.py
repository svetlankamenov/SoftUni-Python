width = int(input())
height = int(input())
cake_pieces = width * height

while cake_pieces > 0:
    pieces = input()

    if pieces == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    pieces = int(pieces)
    cake_pieces -= pieces

    if cake_pieces < 0:
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break