students = {}

n = int(input())

for _ in range(n):
    student, grade = tuple(input().split(" "))
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades)/len(grades)
    print(f"{student} -> {' '.join(f'{gr:.2f}' for gr in grades)} (avg: {average_grade:.2f})")