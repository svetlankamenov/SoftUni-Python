import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

free_time = break_duration - (3 * break_duration / 8)

if free_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(free_time-episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_duration-free_time)} more minutes.")