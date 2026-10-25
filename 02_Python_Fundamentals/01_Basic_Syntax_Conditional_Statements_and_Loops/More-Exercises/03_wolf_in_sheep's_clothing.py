animals = input().split(", ")
wolf_position = animals.index("wolf")
victim_position = len(animals) - wolf_position - 1

if wolf_position == (len(animals) - 1):
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {victim_position}! You are about to be eaten by a wolf!")