from company_app import filter_companies


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