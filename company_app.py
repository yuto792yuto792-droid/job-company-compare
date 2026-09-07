import csv


def filter_companies(companies, min_salary, max_overtime):
    matched_companies = []

    for company in companies:
        annual_salary = int(company["annual_salary"])
        overtime_hours = int(company["overtime_hours"])

        if annual_salary >= min_salary and overtime_hours <= max_overtime:
            matched_companies.append(company)

    return matched_companies


def main():
    min_salary = int(input("希望する最低年収を入力してください: "))
    max_overtime = int(input("希望する月の残業時間の上限を入力してください: "))

    with open("companies.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        companies = list(reader)

    matched_companies = filter_companies(
        companies,
        min_salary,
        max_overtime
    )

    if matched_companies:
        for company in matched_companies:
            print(company["name"])
    else:
        print("条件に合う企業はありません")


if __name__ == "__main__":
    main()