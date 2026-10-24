grade = 0.0
average_grade_of_presentation = 0.0
total_average_grade = 0.0
grades_count = 0

judge_count = int(input())

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        print(f"Student's final assessment is {(total_average_grade/grades_count):.2f}.")
        break

    for _ in range(judge_count):
        grade = float(input())
        average_grade_of_presentation += grade
        total_average_grade += grade
        grades_count += 1

    print(f"{presentation_name} - {(average_grade_of_presentation / judge_count):.2f}.")
    average_grade_of_presentation = 0.0