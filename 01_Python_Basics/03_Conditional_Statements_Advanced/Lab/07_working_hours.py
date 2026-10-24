hour = int(input())
day = input()

if (day.lower() == "monday" or day.lower() == "tuesday"
    or day.lower() == "wednesday" or day.lower() == "thursday" or day.lower() == "friday"
    or day.lower() == "saturday"):

    if hour >= 10 and hour <= 18:
        print("open")
    else:
        print("closed")

elif day.lower() == "sunday":
    print("closed")