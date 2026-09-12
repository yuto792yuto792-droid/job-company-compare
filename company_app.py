import csv


def get_valid_number(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("0以上の数字を入力してください")
                continue

            return value

        except ValueError:
            print("数字を入力してください")


def is_valid_company(company):
    try:
        annual_salary = int(company["annual_salary"])
        overtime_hours = int(company["overtime_hours"])

        if annual_salary < 0 or overtime_hours < 0:
            return False

        return True

    except (ValueError, TypeError, KeyError):
        return False


def filter_companies(companies, min_salary, max_overtime):
    matched_companies = []

    for company in companies:
        if not is_valid_company(company):
            continue

        annual_salary = int(company["annual_salary"])
        overtime_hours = int(company["overtime_hours"])

        if annual_salary >= min_salary and overtime_hours <= max_overtime:
            matched_companies.append(company)

    return matched_companies


def calculate_score(company):
    annual_salary = int(company["annual_salary"])
    overtime_hours = int(company["overtime_hours"])

    score = annual_salary / 10 - overtime_hours

    return score


def sort_companies(companies, sort_type):
    if sort_type == "1":
        return sorted(
            companies,
            key=lambda company: int(company["annual_salary"]),
            reverse=True
        )

    if sort_type == "2":
        return sorted(
            companies,
            key=lambda company: int(company["overtime_hours"])
        )

    if sort_type == "3":
        return sorted(
            companies,
            key=calculate_score,
            reverse=True
        )

    return companies


def main():
    min_salary = get_valid_number(
        "希望する最低年収を入力してください: "
    )

    max_overtime = get_valid_number(
        "希望する月の残業時間の上限を入力してください: "
    )

    with open("companies.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        companies = list(reader)

    matched_companies = filter_companies(
        companies,
        min_salary,
        max_overtime
    )

    if not matched_companies:
        print("条件に合う企業はありません")
        return

    print("並び替え方法を選んでください")
    print("1: 年収が高い順")
    print("2: 残業時間が少ない順")
    print("3: 総合スコアが高い順")

    sort_type = input("選択してください: ")

    sorted_companies = sort_companies(
        matched_companies,
        sort_type
    )

    for company in sorted_companies:
        score = calculate_score(company)

        print(
            company["name"],
            f'年収: {company["annual_salary"]}万円',
            f'残業: {company["overtime_hours"]}時間',
            f'スコア: {score:.1f}'
        )


if __name__ == "__main__":
    main()