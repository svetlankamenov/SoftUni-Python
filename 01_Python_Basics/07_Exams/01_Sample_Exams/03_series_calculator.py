import math

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episodes_duration = float(input())

episodes_duration = episodes_duration + (episodes_duration * 0.2)
total_time_for_watching = seasons_count * episodes_count * episodes_duration + (seasons_count * 10)

print(f"Total time needed to watch the {series_name} series is {math.floor(total_time_for_watching)} minutes.")