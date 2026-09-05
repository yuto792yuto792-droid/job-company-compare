import csv
min_salary = int(input("希望する最低年収（万円）を入力してください: "))
max_overtime = int(input("希望する月の残業時間の上限を入力してください: "))
with open("companies.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for company in reader:
        annual_salary = int(company["annual_salary"])
        overtime_hours = int(company["overtime_hours"])

        if annual_salary >= min_salary and overtime_hours <= max_overtime:
            print(company["name"])