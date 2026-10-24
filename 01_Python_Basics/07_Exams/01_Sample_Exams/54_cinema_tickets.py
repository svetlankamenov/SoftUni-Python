total_tickets_count = 0
movie_tickets_count = 0
student_tickets_count = 0
standard_tickets_count = 0
kids_tickets_count = 0

while True:
    movie_name = input()

    #Докато се въвеждат имена на филми
    if not movie_name == "Finish":
        free_seats = int(input())

        for _ in range(free_seats):
            ticket_type = input()

            if ticket_type == "student":
                student_tickets_count += 1
                movie_tickets_count += 1
            elif ticket_type == "standard":
                standard_tickets_count += 1
                movie_tickets_count += 1
            elif ticket_type == "kid":
                kids_tickets_count += 1
                movie_tickets_count += 1

            if ticket_type == "End":
                break

        print(f"{movie_name} - {(movie_tickets_count/free_seats*100):.2f}% full.")
        total_tickets_count += movie_tickets_count
        movie_tickets_count = 0
    #Когато се въведе Finish
    else:
        print(f"Total tickets: {total_tickets_count}")
        print(f"{(student_tickets_count/total_tickets_count*100):.2f}% student tickets.")
        print(f"{(standard_tickets_count/total_tickets_count*100):.2f}% standard tickets.")
        print(f"{(kids_tickets_count/total_tickets_count*100):.2f}% kids tickets.")
        break