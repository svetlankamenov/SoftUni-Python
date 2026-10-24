average_score = 0.0
problems_count = 0
last_problem = ""
failures = 0

failed_grades_count = int(input())

while True:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {(average_score / problems_count):.2f}")
        print(f"Number of problems: {problems_count}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        failures += 1
        if failed_grades_count == failures:
            print(f"You need a break, {failures} poor grades.")
            break

    average_score += grade
    problems_count += 1
    last_problem = problem_name