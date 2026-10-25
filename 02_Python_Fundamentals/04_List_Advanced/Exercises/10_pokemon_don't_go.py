def distances_update(dist: list, element: int):
    dist = [(x + element) if x <= element else (x - element) for x in dist]
    return dist

distances = input().split(" ")
distances = list(map(int, distances))
sum_of_removed_elements = 0

while True:
    index = int(input())

    if -1 < index < len(distances):
        removed_element = distances.pop(index)
        distances = distances_update(distances, removed_element)
        sum_of_removed_elements += removed_element

    elif index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[len(distances) - 1])
        distances = distances_update(distances, removed_element)
        sum_of_removed_elements += removed_element

    elif index >= len(distances):
        removed_element = distances.pop(len(distances) - 1)
        distances.append(distances[0])
        distances = distances_update(distances, removed_element)
        sum_of_removed_elements += removed_element

    if len(distances) == 0:
        print(sum_of_removed_elements)
        break