import math

free_days = int(input())

play = ((365 - free_days) * 63) + (free_days * 127)
difference = abs(30000 - play)

hours = difference / 60
hours = math.floor(hours)
minutes = difference % 60

if play <= 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
