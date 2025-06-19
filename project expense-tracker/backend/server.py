from fastapi import FastAPI, HTTPException
from datetime import datetime, date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date

class MonthYear(BaseModel):
    year: int
    month: int


# ✅ GET Request for Expenses
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.get_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from database.")
    return expenses


# ✅ POST Request for Expenses
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from database.")
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expense updated successfully"}


# ✅ POST Request for Analytics
@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from database.")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        breakdown[row["category"]] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown


# ✅ POST Request for Analytics (Month-wise)
@app.post("/analytics/monthwise/")
def get_monthly_analytics(month_year: MonthYear):
    try:
        # Format the first and last date of the month
        start_date = datetime(month_year.year, month_year.month, 1)
        if month_year.month == 12:
            end_date = datetime(month_year.year + 1, 1, 1)
        else:
            end_date = datetime(month_year.year, month_year.month + 1, 1)

        # Fetch data from database for the given month
        data = db_helper.fetch_expense_summary(start_date, end_date)

        if not data:
            raise HTTPException(status_code=404, detail="No data found for the specified month.")

        # Compute total and breakdown by category
        total = sum(row['total'] for row in data)
        breakdown = {
            row["category"]: {
                "total": row['total'],
                "percentage": (row['total'] / total) * 100 if total != 0 else 0
            }
            for row in data
        }

        return breakdown

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve data: {str(e)}")