def add_lesson(lesson: str, schedule: list):
    if lesson not in schedule:
        schedule.append(lesson)

    return schedule

def insert_lesson(lesson: str, index: int, schedule: list):
    if lesson not in schedule:
        schedule.insert(index, lesson)

    return schedule

def remove_lesson(lesson: str, schedule: list):
    if lesson in schedule:
        schedule.remove(lesson)
        if f"{lesson}-Exercise" in schedule:
            schedule.remove(f"{lesson}-Exercise")

    return schedule

def swap_lessons(lesson_1: str, lesson_2: str, schedule: list):
    if lesson_1 in schedule and lesson_2 in schedule:
        index_1 = schedule.index(lesson_1)
        index_2 = schedule.index(lesson_2)

        schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

        if f"{lesson_1}-Exercise" in schedule:
            schedule.remove(f"{lesson_1}-Exercise")
            index_1 = schedule.index(lesson_1)
            schedule.insert(index_1+1, f"{lesson_1}-Exercise")
        if f"{lesson_2}-Exercise" in schedule:
            schedule.remove(f"{lesson_2}-Exercise")
            index_2 = schedule.index(lesson_2)
            schedule.insert(index_2+1, f"{lesson_2}-Exercise")

    return schedule

def add_exercise(exercise: str, schedule: list):
    flag = sum(1 for lessons in schedule if exercise in lessons)

    if flag == 1 and exercise in schedule:
        index = schedule.index(exercise)
        schedule.insert(index+1, f"{exercise}-Exercise")
    elif flag == 0:
        schedule.append(exercise)
        schedule.append(f"{exercise}-Exercise")

    return schedule

initial_schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        for i in range(len(initial_schedule)):
            print(f"{i+1}.{initial_schedule[i]}")
        break

    command = command.split(":")

    if command[0] == "Add":
        initial_schedule = add_lesson(command[1], initial_schedule)
    elif command[0] == "Insert":
        initial_schedule = insert_lesson(command[1], int(command[2]), initial_schedule)
    elif command[0] == "Remove":
        initial_schedule = remove_lesson(command[1], initial_schedule)
    elif command[0] == "Swap":
        initial_schedule = swap_lessons(command[1], command[2], initial_schedule)
    elif command[0] == "Exercise":
        initial_schedule = add_exercise(command[1], initial_schedule)

