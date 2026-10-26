import string

line_counter = 1
letters_count = 0
punctuation_marks_counter = 0

file_for_reading = open("text.txt", "r")
file_for_writing = open("output.txt", "w")

for line in file_for_reading:
    for char in line:
        if char in string.punctuation:
            punctuation_marks_counter += 1
        elif char.isalpha():
            letters_count += 1
        elif char == "\n":
            continue

    file_for_writing.write(f"Line {line_counter}: {line} ({letters_count})({punctuation_marks_counter})\n")
    line_counter += 1
    letters_count = 0
    punctuation_marks_counter = 0

file_for_reading.close()
file_for_writing.close()