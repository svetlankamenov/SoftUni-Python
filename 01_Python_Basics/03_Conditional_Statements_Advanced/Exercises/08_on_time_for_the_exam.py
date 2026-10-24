exam_hours = int(input())
exam_minutes = int(input())
arriving_hours = int(input())
arriving_minutes = int(input())

exam_minutes = exam_minutes + exam_hours * 60
arriving_minutes = arriving_minutes + arriving_hours * 60
minutes_difference = exam_minutes - arriving_minutes

if not minutes_difference == 0:
    #Early
    #Подраняване с по-малко от час
    if 30 < minutes_difference < 60:
        print("Early")
        print(f"{minutes_difference} minutes before the start")
    #Подраняване с повече от час
    elif minutes_difference >= 60:
        print("Early")
        print(f"{minutes_difference//60}:{minutes_difference%60:02d} hours before the start")
    #On time 1 case
    elif 0 < minutes_difference <= 30:
        print("On time")
        print(f"{minutes_difference} minutes before the start")
    #Late
    #Закъснение под час
    elif -60 < minutes_difference < 0:
        print("Late")
        print(f"{abs(minutes_difference)} minutes after the start")
    #Закъснение повече от или час
    elif minutes_difference <= -60:
        minutes_difference = abs(minutes_difference)
        print("Late")
        print(f"{minutes_difference//60}:{minutes_difference%60:02d} hours after the start")
#On time 2 case
else:
    print("On time")