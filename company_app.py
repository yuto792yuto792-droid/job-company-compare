import csv

with open("companies.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for company in reader:
        annual_salary = int(company["annual_salary"])
        overtime_hours = int(company["overtime_hours"])

        if annual_salary >= 700 and overtime_hours <= 20:
            print(company["name"])