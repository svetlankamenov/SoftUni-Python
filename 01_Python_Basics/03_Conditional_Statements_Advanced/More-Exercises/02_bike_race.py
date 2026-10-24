juniors_count = int(input())
seniors_count = int(input())
trace_type = input()
profit = 0.0

if trace_type.lower() == "trail":
    profit = juniors_count * 5.50 + seniors_count * 7.00
elif trace_type.lower() == "cross-country":
    profit = juniors_count * 8.00 + seniors_count * 9.50
    if juniors_count + seniors_count >= 50:
        profit *= 0.75
elif trace_type.lower() == "downhill":
    profit = juniors_count * 12.25 + seniors_count * 13.75
elif trace_type.lower() == "road":
    profit = juniors_count * 20.00 + seniors_count * 21.50

profit *= 0.95

print(f"{profit:.2f}")