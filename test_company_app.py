from company_app import (
    filter_companies,
    sort_companies,
    calculate_score,
    get_valid_number,
    is_valid_company,
    filter_by_industry,
    filter_by_location,
    add_favorite

)

def test_filter_companies():
    companies = [
        {
            "name": "A社",
            "annual_salary": "600",
            "overtime_hours": "10"
        },
        {
            "name": "B社",
            "annual_salary": "450",
            "overtime_hours": "30"
        }
    ]

    result = filter_companies(
        companies,
        min_salary=500,
        max_overtime=20
    )

    assert len(result) == 1
    assert result[0]["name"] == "A社"


def test_filter_companies_no_matches():
    companies = [
        {
            "name": "A社",
            "annual_salary": "600",
            "overtime_hours": "10"
        },
        {
            "name": "B社",
            "annual_salary": "450",
            "overtime_hours": "30"
        }
    ]

    result = filter_companies(
        companies,
        min_salary=1000,
        max_overtime=5
    )

    assert result == []


def test_sort_companies_by_salary():
    companies = [
        {
            "name": "A社",
            "annual_salary": "500",
            "overtime_hours": "10"
        },
        {
            "name": "B社",
            "annual_salary": "700",
            "overtime_hours": "20"
        },
        {
            "name": "C社",
            "annual_salary": "600",
            "overtime_hours": "15"
        }
    ]

    result = sort_companies(companies, "1")

    assert result[0]["name"] == "B社"
    assert result[1]["name"] == "C社"
    assert result[2]["name"] == "A社"


def test_sort_companies_by_overtime():
    companies = [
        {
            "name": "A社",
            "annual_salary": "500",
            "overtime_hours": "20"
        },
        {
            "name": "B社",
            "annual_salary": "700",
            "overtime_hours": "10"
        },
        {
            "name": "C社",
            "annual_salary": "600",
            "overtime_hours": "15"
        }
    ]

    result = sort_companies(companies, "2")

    assert result[0]["name"] == "B社"
    assert result[1]["name"] == "C社"
    assert result[2]["name"] == "A社"


def test_calculate_score():
    company = {
        "name": "A社",
        "annual_salary": "700",
        "overtime_hours": "20"
    }

    result = calculate_score(company)

    assert result == 50.0


def test_sort_companies_by_score():
    companies = [
        {
            "name": "A社",
            "annual_salary": "600",
            "overtime_hours": "10"
        },
        {
            "name": "B社",
            "annual_salary": "700",
            "overtime_hours": "30"
        },
        {
            "name": "C社",
            "annual_salary": "650",
            "overtime_hours": "5"
        }
    ]

    result = sort_companies(companies, "3")

    assert result[0]["name"] == "C社"
    assert result[1]["name"] == "A社"
    assert result[2]["name"] == "B社"

def test_get_valid_number(monkeypatch):
    inputs = iter(["abc", "-100", "500"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    result = get_valid_number("数字を入力してください: ")

    assert result == 500

def test_is_valid_company():
    valid_company = {
        "name": "A社",
        "annual_salary": "600",
        "overtime_hours": "10"
    }

    invalid_salary = {
        "name": "B社",
        "annual_salary": "",
        "overtime_hours": "10"
    }

    invalid_overtime = {
        "name": "C社",
        "annual_salary": "600",
        "overtime_hours": "abc"
    }

    negative_value = {
        "name": "D社",
        "annual_salary": "-100",
        "overtime_hours": "10"
    }

    assert is_valid_company(valid_company) is True
    assert is_valid_company(invalid_salary) is False
    assert is_valid_company(invalid_overtime) is False
    assert is_valid_company(negative_value) is False

def test_filter_companies_skips_invalid_data():
    companies = [
        {
            "name": "A社",
            "annual_salary": "600",
            "overtime_hours": "10"
        },
        {
            "name": "B社",
            "annual_salary": "",
            "overtime_hours": "20"
        },
        {
            "name": "C社",
            "annual_salary": "700",
            "overtime_hours": "abc"
        }
    ]

    result = filter_companies(
        companies,
        min_salary=500,
        max_overtime=20
    )

    assert len(result) == 1
    assert result[0]["name"] == "A社"

def test_filter_by_industry():
    companies = [
        {
            "name": "A社",
            "industry": "IT",
            "annual_salary": "600",
            "overtime_hours": "10",
            "location": "東京"
        },
        {
            "name": "B社",
            "industry": "金融",
            "annual_salary": "700",
            "overtime_hours": "20",
            "location": "東京"
        },
        {
            "name": "C社",
            "industry": "IT",
            "annual_salary": "650",
            "overtime_hours": "15",
            "location": "大阪"
        }
    ]

    result = filter_by_industry(companies, "IT")

    assert len(result) == 2
    assert result[0]["name"] == "A社"
    assert result[1]["name"] == "C社"

def test_filter_by_industry_no_selection():
    companies = [
        {
            "name": "A社",
            "industry": "IT"
        },
        {
            "name": "B社",
            "industry": "金融"
        }
    ]

    result = filter_by_industry(companies, "")

    assert result == companies

def test_filter_by_location():
    companies = [
        {
            "name": "A社",
            "location": "東京"
        },
        {
            "name": "B社",
            "location": "大阪"
        },
        {
            "name": "C社",
            "location": "東京"
        }
    ]

    result = filter_by_location(companies, "東京")

    assert len(result) == 2
    assert result[0]["name"] == "A社"
    assert result[1]["name"] == "C社"


def test_filter_by_location_no_selection():
    companies = [
        {
            "name": "A社",
            "location": "東京"
        },
        {
            "name": "B社",
            "location": "大阪"
        }
    ]

    result = filter_by_location(companies, "")

    assert result == companies

def test_add_favorite():
    companies = [
        {
            "name": "A社"
        },
        {
            "name": "B社"
        }
    ]

    result = add_favorite(companies, "B社")

    assert result is not None
    assert result["name"] == "B社"

def test_add_favorite_not_found():
    companies = [
        {
            "name": "A社"
        },
        {
            "name": "B社"
        }
    ]

    result = add_favorite(companies, "C社")

    assert result is None