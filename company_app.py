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


def filter_by_industry(companies, industry):
    if industry == "":
        return companies

    return [
        company
        for company in companies
        if company["industry"] == industry
    ]


def filter_by_location(companies, location):
    if location == "":
        return companies

    return [
        company
        for company in companies
        if company["location"] == location
    ]


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


def add_favorite(companies, company_name):
    for company in companies:
        if company["name"] == company_name:
            return company

    return None


def main():
    min_salary = get_valid_number(
        "希望する最低年収を入力してください: "
    )

    max_overtime = get_valid_number(
        "希望する月の残業時間の上限を入力してください: "
    )

    industry = input(
        "希望する業界を入力してください（指定なしはEnter）: "
    )

    location = input(
        "希望する勤務地を入力してください（指定なしはEnter）: "
    )

    with open("companies.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        companies = list(reader)

    matched_companies = filter_companies(
        companies,
        min_salary,
        max_overtime
    )

    matched_companies = filter_by_industry(
        matched_companies,
        industry
    )

    matched_companies = filter_by_location(
        matched_companies,
        location
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

    print("\n検索結果")

    for company in sorted_companies:
        score = calculate_score(company)

        print(
            company["name"],
            f'業界: {company["industry"]}',
            f'年収: {company["annual_salary"]}万円',
            f'残業: {company["overtime_hours"]}時間',
            f'勤務地: {company["location"]}',
            f'スコア: {score:.1f}'
        )

    favorite_name = input(
        "\nお気に入りに追加する企業名を入力してください"
        "（追加しない場合はEnter）: "
    )

    favorites = []

    if favorite_name != "":
        favorite = add_favorite(
            sorted_companies,
            favorite_name
        )

        if favorite is not None:
            favorites.append(favorite)
            print(f"{favorite_name}をお気に入りに追加しました")
        else:
            print("その企業は検索結果にありません")

    if favorites:
        print("\nお気に入り企業")

        for company in favorites:
            print(company["name"])


if __name__ == "__main__":
    main()