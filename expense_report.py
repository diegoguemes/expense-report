import locale
from enum import Enum, unique, auto
from datetime import datetime
from typing import List


@unique
class ExpenseType(Enum):
    DINNER = auto()
    BREAKFAST = auto()
    CAR_RENTAL = auto()


class Expense:
    type: ExpenseType
    amount: int

    def name(self):
        name = ""
        if self.type == ExpenseType.DINNER:
            name = "Dinner"
        elif self.type == ExpenseType.BREAKFAST:
            name = "Breakfast"
        elif self.type == ExpenseType.CAR_RENTAL:
            name = "Car Rental"
        return name
    
    def is_over_expense(self):
        return self.type == ExpenseType.DINNER and self.amount > 5000 or self.type == ExpenseType.BREAKFAST and self.amount > 1000

    def is_meal(self):
        return self.type == ExpenseType.DINNER or self.type == ExpenseType.BREAKFAST

class ExpenseReportPrinter:
    def print_report(self, expenses: List[Expense]):
        report = ExpenseReport(expenses)

        # TODO: Reemplazar con datetime.now()
        print("Expense Report", datetime(2023, 10, 3))

        for expense in report.expenses:
            meal_over_expenses_marker = "X" if expense.is_over_expense() else " "
            print(expense.name(), "\t", expense.amount, "\t", meal_over_expenses_marker)

        print("Meals:", report.calculate_meals_total())
        print("Total:", report.calculate_total())


class ExpenseReport():
    def __init__(self, expenses: List[Expense]) -> None:
        self.expenses = expenses
    def calculate_meals_total(self) -> int:
        meals = 0
        for expense in self.expenses:
            if expense.is_meal():
                meals += expense.amount
        return meals

    def calculate_total(self) -> int:
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

