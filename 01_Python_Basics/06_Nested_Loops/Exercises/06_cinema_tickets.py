total_ticket_count = 0
student_ticket_count = 0
standard_ticket_count = 0
kids_ticket_count = 0
people_in_hall = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        print(f"Total tickets: {total_ticket_count}")
        print(f"{(student_ticket_count/total_ticket_count*100):.2f}% student tickets.")
        print(f"{(standard_ticket_count/total_ticket_count*100):.2f}% standard tickets.")
        print(f"{(kids_ticket_count/total_ticket_count*100):.2f}% kids tickets.")

        break

    free_seats = int(input())

    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_ticket_count += 1
            total_ticket_count += 1
            people_in_hall += 1

        elif ticket_type == "standard":
            standard_ticket_count += 1
            total_ticket_count += 1
            people_in_hall += 1

        elif ticket_type == "kid":
            kids_ticket_count += 1
            total_ticket_count += 1
            people_in_hall += 1

    print(f"{movie_name} - {(people_in_hall/free_seats*100):.2f}% full.")
    people_in_hall = 0