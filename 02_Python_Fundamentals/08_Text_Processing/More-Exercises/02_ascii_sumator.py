sum = 0
start_i = ord(input())
end_i = ord(input())
string = input()

for ch in string:
    if start_i < ord(ch) < end_i:
        sum += ord(ch)

print(sum)