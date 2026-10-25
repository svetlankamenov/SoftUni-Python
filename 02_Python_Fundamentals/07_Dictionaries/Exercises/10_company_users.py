companies_info = {}

while True:
    line = input()
    if line == "End":
        for company_name in companies_info.keys():
            print(f"{company_name}")
            for employee_id in companies_info[company_name]:
                print(f"-- {employee_id}")
        break

    company_name, employee_id = line.split(" -> ")

    if company_name not in companies_info:
        companies_info[company_name] = [employee_id]
    else:
        if employee_id not in companies_info[company_name]:
            companies_info[company_name].append(employee_id)