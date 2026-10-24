school_class = 1
average_grade = 0.0
expelled_flag = 0

student_name = input()

while True:
    if expelled_flag == 2:
        print(f"{student_name} has been excluded at {school_class} grade")
        break
    if school_class == 13:
        print(f"{student_name} graduated. Average grade: {(average_grade/12):.2f}")
        break

    grade = float(input())

    if grade >= 4.00:
        average_grade += grade
        school_class += 1
    else:
        expelled_flag += 1
        continue

