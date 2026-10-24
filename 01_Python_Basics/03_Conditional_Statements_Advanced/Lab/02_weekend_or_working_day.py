day = input()

if (day.lower() == "monday" or day.lower() == "tuesday" or day.lower() == "wednesday"
    or day.lower() == "thursday" or day.lower() == "friday"):
    print("Working day")
elif day.lower() == "saturday" or day.lower() == "sunday":
    print("Weekend")
else:
    print("Error")