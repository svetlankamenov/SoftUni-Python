def print_row(size:int, star_count:int):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")

size_of_figure = int(input())
for star_count in range(1, size_of_figure):
    print_row(size_of_figure, star_count)
for star_count in range(size_of_figure, 0, -1):
    print_row(size_of_figure, star_count)