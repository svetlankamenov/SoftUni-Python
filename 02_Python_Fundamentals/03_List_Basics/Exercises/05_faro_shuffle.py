shuffled_cards = []

cards = input().split(" ")
shuffles_count = int(input())

for _ in range(shuffles_count):
    first_half = cards[:len(cards) // 2]
    second_half = cards[len(cards) // 2:]

    for i in range(len(first_half)):
        shuffled_cards.append(first_half[i])
        shuffled_cards.append(second_half[i])

    cards = shuffled_cards
    shuffled_cards = []

print(cards)