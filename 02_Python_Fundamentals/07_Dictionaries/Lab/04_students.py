students = {}

while True:
    student_info = input()
    if ":" in student_info:
        name, ID, course = student_info.split(":")
        students[name] = {}
        students[name]["ID"] = int(ID)
        students[name]["course"] = course
    else:
        course_name = " ".join(student_info.split("_"))
      
        for student_name, info in students.items():
            if info["course"] == course_name:
                print(f"{student_name} - {info['ID']}")
        break