kilometers = int(input())
time_of_day = input()

taxi = 0.0
buss = 0.0
train = 0.0

if time_of_day.lower() == "day":
    taxi = 0.70 + (0.79 * kilometers)
    buss = 0.09 * kilometers
    train = 0.06 * kilometers
elif time_of_day.lower() == "night":
    taxi = 0.70 + (0.90 * kilometers)
    buss = 0.09 * kilometers
    train = 0.06 * kilometers

if kilometers >= 100:
    if taxi < buss and taxi < train:
        print(f"{taxi:.2f}")
    elif buss < taxi and buss < train:
        print(f"{buss:.2f}")
    else:
        print(f"{train:.2f}")
elif kilometers >= 20 and kilometers < 100:
    if taxi < buss:
        print(f"{taxi:.2f}")
    else:
        print(f"{buss:.2f}")
else:
    print(f"{taxi:.2f}")