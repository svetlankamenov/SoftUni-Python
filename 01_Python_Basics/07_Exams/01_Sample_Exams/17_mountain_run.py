import math

climbing_record = float(input())
length = float(input())
meter_per_second = float(input())

seconds_delay = math.floor(length / 50) * 30

climbing_time = length * meter_per_second + seconds_delay

if climbing_time < climbing_record:
    print(f"Yes! The new record is {climbing_time:.2f} seconds.")
else:
    print(f"No! He was {abs(climbing_time-climbing_record):.2f} seconds slower.")