def add_a_card(card: str, lst:list):
    lst.append(card)
    return lst

def remove_a_card(card: str, lst:list):
    lst.remove(card)
    return lst

def remove_by_index(i: str, lst:list):
    i = int(i)
    lst.pop(i)
    return lst

def insert_a_card(card: str, i: str, lst:list):
    i = int(i)
    lst.insert(i, card)
    return lst

cards = input().split(", ")
n = int(input())

for _ in range(n):
    command = input()
    command = command.split(", ")

    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            cards = add_a_card(command[1], cards)
            print("Card successfully added")

    elif command[0] == "Remove":
        if command[1] not in cards:
            print("Card not found")
        else:
            cards = remove_a_card(command[1], cards)
            print("Card successfully removed")

    elif command[0] == "Remove At":
        if not 0 <= int(command[1]) < len(cards):
            print("Index out of range")
        else:
            cards = remove_by_index(command[1], cards)
            print("Card successfully removed")

    elif command[0] == "Insert":
        if not 0 <= int(command[1]) < len(cards):
            print("Index out of range")
        elif command[2] in cards:
            print("Card is already added")
        else:
            cards = insert_a_card(command[2], command[1], cards)
            print("Card successfully added")

cards_collection = ", ".join(cards)
print(cards_collection)