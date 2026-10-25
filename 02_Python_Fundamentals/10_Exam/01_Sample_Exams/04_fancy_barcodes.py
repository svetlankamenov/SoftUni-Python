import re

pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

barcodes = []

n = int(input())
for _ in range(n):
    barcodes.append(input())

for barcode in barcodes:
    if re.fullmatch(pattern, barcode):
        group = "".join(re.findall(r"\d+", barcode)) or "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")