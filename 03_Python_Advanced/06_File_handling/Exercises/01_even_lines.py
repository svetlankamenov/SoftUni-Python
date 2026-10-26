file = open("text.txt","r")
symbols = {"-", ",", ".", "!", "?"}
counter = 0
corrected_line = ""

for line in file:
    if counter % 2 == 0:
        for char in line:
            if char in symbols:
                corrected_line += "@"
            elif char == "\n":
                pass
            else:
                corrected_line += char

        corrected_line = corrected_line.split(" ")
        print(" ".join(corrected_line[::-1]))

    counter += 1
    corrected_line = ""

file.close()