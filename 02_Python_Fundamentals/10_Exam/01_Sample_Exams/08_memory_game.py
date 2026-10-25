elements = input().split(" ")
moves = 1

while True:
    indexes = input()
    if indexes == "end":
        if len(elements) == 0:
            print(f"You have won in {moves} turns!")
            break
        else:
            print("Sorry you lose :(")
            print(" ".join(elements))
            break

    indexes = indexes.split(" ")
    in_1, in_2 = int(indexes[0]), int(indexes[1])

    if (in_1 == in_2) or not (0 <= in_1 < len(elements)) or not (0 <= in_2 < len(elements)):
        elements.insert(len(elements)//2, f"-{moves}a")
        elements.insert(len(elements)//2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if elements[in_1] == elements[in_2]:
        element = elements[in_1]
        print(f"Congrats! You have found matching elements - {element}!")
        elements.remove(element)
        elements.remove(element)
    elif elements[in_1] != elements[in_2]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    moves += 1