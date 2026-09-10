from company_app import filter_companies, sort_companies, calculate_score


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