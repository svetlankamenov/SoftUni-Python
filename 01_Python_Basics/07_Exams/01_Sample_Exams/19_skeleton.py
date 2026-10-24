control_minutes = int(input())
control_seconds = int(input())
length = float(input())
speed = int(input())

control_time = control_minutes * 60 + control_seconds
gained_time = length / 120 * 2.5

competitor_time = ((length / 100) * speed) - gained_time

if competitor_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {competitor_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(competitor_time-control_time):.3f} second slower.")
