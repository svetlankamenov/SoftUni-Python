movie_name = ""
movie_rating = 0.0
average_rating = 0.0
highest_rating = 0.0
lowest_rating = 0.0
movie_with_highest_rating = ""
movie_with_lowest_rating = ""

movies_count = int(input())

for _ in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    average_rating += movie_rating

    if _ == 0:
        highest_rating = movie_rating
        movie_with_highest_rating = movie_name
        lowest_rating = movie_rating
        movie_with_lowest_rating = movie_name
        continue

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        movie_with_highest_rating = movie_name

    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        movie_with_lowest_rating = movie_name

print(f"{movie_with_highest_rating} is with highest rating: {highest_rating:.1f}")
print(f"{movie_with_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {(average_rating / movies_count):.1f}")