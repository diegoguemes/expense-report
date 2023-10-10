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


class ExpenseReport:
    def print_report(self, expenses: List[Expense]):
        total = 0
        meals = 0

        # TODO: Reemplazar con datetime.now()
        print("Expense Report", datetime(2023, 10, 3))

        for expense in expenses:
            if self.is_meal(expense):
                meals += expense.amount

            name = self.expense_name(expense)

            meal_over_expenses_marker = "X" if self.is_over_expense(expense) else " "
            print(name, "\t", expense.amount, "\t", meal_over_expenses_marker)
            total += expense.amount

        print("Meals:", meals)
        print("Total:", total)

    def expense_name(self, expense):
        name = ""
        if expense.type == ExpenseType.DINNER:
            name = "Dinner"
        elif expense.type == ExpenseType.BREAKFAST:
            name = "Breakfast"
        elif expense.type == ExpenseType.CAR_RENTAL:
            name = "Car Rental"
        return name

    def is_over_expense(self, expense):
        return expense.type == ExpenseType.DINNER and expense.amount > 5000 or expense.type == ExpenseType.BREAKFAST and expense.amount > 1000

    def is_meal(self, expense):
        return expense.type == ExpenseType.DINNER or expense.type == ExpenseType.BREAKFAST