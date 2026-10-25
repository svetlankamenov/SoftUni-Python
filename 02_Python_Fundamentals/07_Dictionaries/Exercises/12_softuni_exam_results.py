exam_results = {}
language_submissions = {}

def add_result(name: str, subject: str, score: int, results: dict, subjects: dict):
    if name not in results:
        results[name] = {subject: score}
    else:
        if subject not in results[name].keys():
            results[name][subject] = score
        else:
            if results[name][subject] < score:
                results[name][subject] = score

    if subject not in subjects:
        subjects[subject] = 1
    else:
        subjects[subject] += 1

    return results, subjects

def ban_student(name: str, results: dict):
    if name in results:
        del results[name]

    return results

def print_results(results: dict, subjects: dict):
    print("Results:")
    for name in results.keys():
        for subject in results[name].keys():
            print(f"{name} | {results[name][subject]}")
    print("Submissions:")
    for subject, submissions in subjects.items():
        print(f"{subject} - {submissions}")

while True:
    line = input()
    if line == "exam finished":
        print_results(exam_results, language_submissions)
        break

    if "banned" not in line:
        username, language, points = line.split("-")
        exam_results, language_submissions = add_result(username, language, int(points), exam_results, language_submissions)
    else:
        line = line.split("-")
        username = line[0]
        exam_results = ban_student(username, exam_results)