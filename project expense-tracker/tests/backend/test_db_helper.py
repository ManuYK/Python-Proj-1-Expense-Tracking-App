from backend import db_helper
def test_get_expenses_for_date():
    expenses = db_helper.get_expenses_for_date("2024-08-01")

    assert len(expenses) == 4



