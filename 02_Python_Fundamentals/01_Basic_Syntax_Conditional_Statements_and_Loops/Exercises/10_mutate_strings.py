first_string = input()
second_string = input()
new_string = ""
string_list = []

for i in range(len(first_string)+1):
    new_string = second_string[:i] + first_string[i:]

    string_list.append(new_string)
    new_string = ""

string_list = list(dict.fromkeys(string_list))
string_list.remove(first_string)

for i in range(len(string_list)):
    print(string_list[i])