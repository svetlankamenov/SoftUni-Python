day = input()

if day.lower() == "monday" or day.lower() == "tuesday" or day.lower() == "friday":
    print(12)
elif day.lower() == "wednesday" or day.lower() == "thursday":
    print(14)
elif day.lower() == "saturday" or day.lower() == "sunday":
    print(16)
