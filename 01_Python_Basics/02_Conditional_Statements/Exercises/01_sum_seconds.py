first_athlete = int(input())
second_athlete = int(input())
third_athlete = int(input())
minutes = 0
seconds = 0

total_time = first_athlete + second_athlete + third_athlete
minutes = total_time // 60
seconds = total_time % 60

if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")