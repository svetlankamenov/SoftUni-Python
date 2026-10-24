bitcoins = int(input())
chinese_yuan = float(input())
commision = float(input())

euro = bitcoins * 1168 / 1.95
euro += chinese_yuan * 0.15 * 1.76 / 1.95
euro *= (1 - commision/100)

print(f"{euro:.2f}")