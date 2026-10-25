first_lst = []
filtered_lst = []

n = int(input())
key_word = input()

for _ in range(n):
    first_lst.append(input())

for string in first_lst:
    if key_word in string:
        filtered_lst.append(string)

print(first_lst)
print(filtered_lst)