movie_name = input()
days_projection = int(input())
tickets_count = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())

profit = days_projection * (tickets_count * ticket_price)
profit = profit - (profit * percentage_for_cinema / 100)

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")