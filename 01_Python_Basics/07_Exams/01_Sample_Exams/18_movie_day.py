filming_time = int(input())
scenes_count = int(input())
scene_duration = int(input())

filming_duration = scenes_count * scene_duration
terrain_preparation = filming_time * 0.15
filming_duration += terrain_preparation

if filming_duration <= filming_time:
    print(f"You managed to finish the movie on time! You have {round(abs(filming_duration-filming_time))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(abs(filming_duration-filming_time))} minutes.")