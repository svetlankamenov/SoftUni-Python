total_expense = 0.0

kozunak_count = int(input())
eggshell_count = int(input())
cookies_kilos = int(input())

total_expense = ((kozunak_count * 3.20) + (eggshell_count * 4.35) +
                 (12 * eggshell_count * 0.15) + (cookies_kilos * 5.40))

print(f"{total_expense:.2f}")