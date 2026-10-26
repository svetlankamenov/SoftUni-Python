from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
main_colors_found = []
secondary_colors_found = []
found_colors = []

line = deque(input().split(" "))

while line:

    if len(line) == 1:
        if line[0] in main_colors:
            color = line.pop()
            main_colors_found.append(color)
            found_colors.append(color)
        elif line[0] in secondary_colors:
            color = line.pop()
            secondary_colors_found.append(color)
            found_colors.append(color)
        else:
            line.pop()
    else:
        first = line.popleft()
        last = line.pop()

        if (first + last) in main_colors:
            main_colors_found.append(first+last)
            found_colors.append(first+last)
        elif (last + first) in main_colors:
            main_colors_found.append(last+first)
            found_colors.append(last+first)
        elif (first + last) in secondary_colors:
            secondary_colors_found.append(first+last)
            found_colors.append(first+last)
        elif (last + first) in secondary_colors:
            secondary_colors_found.append(last+first)
            found_colors.append(last+first)
        else:
            first = first[:(len(first)-1)]
            last = last[:(len(last)-1)]
            i = len(line) // 2
            if first != "":
                line.insert(i, first)
                i +=1
            if last != "":
                line.insert(i, last)

for color in secondary_colors_found:
    if color == "orange":
        if not ("red" in main_colors_found and "yellow" in main_colors_found):
            found_colors.remove(color)
    elif color == "purple":
        if not ("red" in main_colors_found and "blue" in main_colors_found):
            found_colors.remove(color)
    elif color == "green":
        if not ("yellow" in main_colors_found and "blue" in main_colors_found):
            found_colors.remove(color)

print(found_colors)