#ord()
best_movie = ""
best_movie_points = 0
symbols_sum = 0
max_count_of_movies = 0

while True:
    movie_name = input()
    if movie_name == "STOP":
        break

    max_count_of_movies += 1

    for i in movie_name:
        symbol_number = ord(i)
        if "A" <= i <= "Z":
            symbol_number -= len(movie_name)
        elif "a" <= i <= "z":
            symbol_number -= len(movie_name) * 2
        symbols_sum += symbol_number

    if symbols_sum > best_movie_points:
        best_movie = movie_name
        best_movie_points = symbols_sum

    if max_count_of_movies == 7:
        print("The limit is reached.")
        break

    symbols_sum = 0

print(f"The best movie for you is {best_movie} with {best_movie_points} ASCII sum.")