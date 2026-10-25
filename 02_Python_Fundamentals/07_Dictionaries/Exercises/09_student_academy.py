students_info = {}
filtered_students = {}

n = int(input())

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students_info:
        students_info[student_name] = [grade]
    else:
        students_info[student_name].append(grade)

for student in students_info.keys():
    average_grade = sum(students_info[student]) / len(students_info[student])
    if average_grade >= 4.50:
        filtered_students[student] = [average_grade]

for student, grades in filtered_students.items():
    print(f"{student} -> {grades[0]:.2f}")