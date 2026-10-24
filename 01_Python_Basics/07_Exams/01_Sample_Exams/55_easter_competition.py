winner_name = ""
winner_rate = 0
current_rate = 0

easter_breads_count = int(input())

for _ in range(easter_breads_count):
    baker_name = input()

    while True:
        easter_bread_rate = input()
        if easter_bread_rate == "Stop":
            print(f"{baker_name} has {current_rate} points.")
            break
        easter_bread_rate = int(easter_bread_rate)
        current_rate += easter_bread_rate

    if current_rate > winner_rate:
        print(f"{baker_name} is the new number 1!")
        winner_name = baker_name
        winner_rate = current_rate

    current_rate = 0

print(f"{winner_name} won competition with {winner_rate} points!")