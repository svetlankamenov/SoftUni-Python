courses = {}

while True:
    line = input()
    if line == "end":

        for course_name in courses.keys():
            print(f"{course_name}: {len(courses[course_name])}")
            for student_name in courses[course_name]:
                print(f"-- {student_name}")
        break

    course_name, student_name = line.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)