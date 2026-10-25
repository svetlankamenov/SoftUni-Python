def decipher(lst: list, morse_code: dict):
    deciphered_code = ""
    for word in lst:
        deciphered_code += morse_code[word]
    deciphered_code += " "
    return deciphered_code

message = ""
alphabet = {".-" : "A", "-..." : "B", "-.-." : "C", "-.." : "D",
            "." : "E", "..-." : "F", "--." : "G", "...." : "H",
            ".." : "I", ".---" : "J", "-.-" : "K", ".-.." : "L",
            "--" : "M", "-." : "N", "---" : "O", ".--." : "P",
            "--.-" : "Q", ".-." : "R", "..." : "S", "-" : "T",
            "..-" : "U", "...-" : "V", ".--" : "W", "-..-" :
                "X", "-.--" : "Y", "--.." : "Z"}

code = input()
code = code.split(" | ")

for i in range(0, len(code)):
    words = code[i].split()
    message += decipher(words, alphabet)

print(message)