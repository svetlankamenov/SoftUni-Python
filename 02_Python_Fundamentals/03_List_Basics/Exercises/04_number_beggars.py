integers =[]
beggars_sum = []

string_of_integers = input().split(", ")
beggars_count = int(input())

for i in string_of_integers:
    integers.append(int(i))

for _ in range(beggars_count):
    beggars_sum.append(0)

beggars_counter = 0

for number in integers:
    beggars_counter += 1
    beggars_sum[beggars_counter-1] += number
    if beggars_counter == beggars_count:
        beggars_counter = 0

print(beggars_sum)