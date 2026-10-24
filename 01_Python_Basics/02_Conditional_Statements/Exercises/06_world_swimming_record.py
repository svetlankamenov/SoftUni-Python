import math

swim_record = float(input())
length = float(input())
swimming_speed = float(input())

wasted_time = math.floor(length / 15) * 12.5


swimming_time = length * swimming_speed + wasted_time

difference = abs(swimming_time - swim_record)

if swimming_time < swim_record:
    print(f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")