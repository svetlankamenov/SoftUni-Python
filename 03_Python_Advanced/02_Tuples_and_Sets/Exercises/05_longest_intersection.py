intersections = []

n = int(input())

for _ in range(n):
    user_input = input().split("-")

    first_start, first_end = map(int,user_input[0].split(","))
    second_start, second_end = map(int, user_input[1].split(","))

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersections.append(first_set.intersection(second_set))

longest_intersection = max(intersections, key = len)

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")