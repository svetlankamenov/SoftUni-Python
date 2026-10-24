temp = float(input())

if temp <= 35 and temp >= 26 :
    print("Hot")
elif temp <= 25.9 and temp >= 20.1 :
    print("Warm")
elif temp <= 20.0 and temp >= 15.0 :
    print("Mild")
elif temp <= 14.9 and temp >= 12.0 :
    print("Cool")
elif temp <= 11.9 and temp >= 5.0 :
    print("Cold")
else :
    print("unknown")